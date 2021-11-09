#Name: Asif Ahmad
#Date: 11-08-2021
#Summary: Gathers Pull Request details and prints output to terminal and sends email summary.

import requests
import datetime
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tabulate import tabulate
from datetime import date

#A.Ahmad: Asking for initial input information.
print("Hello and Welcome To The GitHub Pull Request Script!")
print()
user_name = input("Enter The Repository Owner Username:")
repo_name = input("Enter The Name of The SPECIFIC Repository :")
receiver_email = input("Enter Email To Also Send Results :")

#A.Ahmad: Declaring variables to be used.
today = date.today()
sender_email = "asifsailpoint7@gmail.com"
port = 465  #A.Ahmad: Port For Gmail SSL.
smtp_server = "smtp.gmail.com"
password = "Miller84!" #A.Ahmad: Hard coding gmail password, bad practice I know!
url = "https://api.github.com/repos/{}/{}/pulls?state=all".format(user_name,repo_name)
repo_url = "https://github.com/{}/{}/".format(user_name,repo_name)
pull_data = requests.get(url).json()
recent_prs = [] #A.Ahmad: List that will store all the recent pull requests.

#A.Ahmad: Prepping data by using a dictionary. 
for repo in pull_data:
  relevant_info = {
    'PR State': repo['state'],
    'PR URL': repo['url'],
    'PR Description': repo['body'],
    'Last_Updated': repo['updated_at']
  }
  d1 = datetime.datetime.strptime(relevant_info['Last_Updated'],"%Y-%m-%dT%H:%M:%SZ")
  relevant_info['Last_Updated'] = d1.strftime('%s')
  
  #A.Ahmad: Logic for adding to recent_prs list if last_updated is within last 7 days.
  if int(time.time()) - int(relevant_info['Last_Updated']) <= 7 * 24 * 60 * 60:
    relevant_info['Last_Updated'] = datetime.datetime.fromtimestamp(int(relevant_info['Last_Updated']))
    recent_prs.append(relevant_info)

#A.Ahmad: Printing out results in table-form in the console.
print()
print("You have requested the Pull Request details for the following repo:")
print (repo_url)
print()
print("Pull Request Results For The Last 7 Days:")
print(tabulate(recent_prs, headers="keys", tablefmt="grid"))

#A.Ahmad: Code for building email.
text = """
Hello, Friend

You have requested the Pull Request details for the following repo:
{repo_url}

Pull Request Results For The Last 7 Days:
{table}

I hope you enjoyed using this awesome python script! Have a nice day!

Regards,
Asif Ahmad
Email: Asif.Ahmad@hotmail.com"""

html = """
<head>
<style>
table, th, td {{ border: 1px solid black; }}
table {{ border-collapse: collapse; }}
th, td {{ padding: 5px; }}
</style>
</head>
<html><body><p>Hello, Friend</p>
<p>You have requested the Pull Request details for the following repo:</p>
{repo_url}

<p>Pull Request Results For The Last 7 Days:</p>
{table}
<p>I hope you enjoyed using this awesome python script! Have a nice day!</p>
<p>Regards,</p>
<p>Asif Ahmad</p>
<p>Email: Asif.Ahmad@hotmail.com</p>
</body></html>
"""
#A.Ahmad: Building and Sending The Email.
text = text.format(table=tabulate(recent_prs, headers="keys", tablefmt="grid"), repo_url=repo_url)
html = html.format(table=tabulate(recent_prs, headers="keys", tablefmt="html"), repo_url=repo_url)

message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html,'html')])

message['Subject'] = "GitHub PR Summary Email!"
message['From'] = sender_email
message['To'] = receiver_email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
