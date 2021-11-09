
# SailPoint Pull-Request Challenge

Python script for capturing pull-request details for a specific github repository. The script utilizes the GitHub API for retrieving the repository information programmatically by user specified owner username and specific github repository name.
 
The script only pulls the information for the past week (7 days) and displas all open, closed, and in-progress pull request details. The output is displayed both in the console (terminal) and a user digestible format is also emailed to the user specified email address.


## Prerequisites
Python 3.10.0 was used in authoring this script and is recommended to be installed to run this script locally. Please visit the following on instructions on how to setup and download Python:
https://www.python.org/downloads/

Also, it is recommended to install a few additional modules (pip install) to make sure things execute smoothly: requests, datetime, time, smtplib, ssl, MIMEMultipart
from email.mime.text import MIMEText, tabulate, date
## Run Locally

Clone the project 

```bash
  git clone https://github.com/asif-sailpoint/challenge.git
```

Go to the project directory

```bash
  cd challenge
```

Run Script

```bash
  /<PYTHON_INSTALL>/python3 SP_challenge.py 
```



## Usage

You can enter your own choices here, below is just an example in terms:

#GitHub Owner:

Enter The Repository Owner Username :Geerlingguy

#Repository Name:

Enter The Name of The SPECIFIC Repository :drupal-vm

#User Email For Results:

Enter Email To Also Send Results :Asif.Ahmad@gmail.com

