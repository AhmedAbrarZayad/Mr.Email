import requests
from bs4 import BeautifulSoup
#for sending email
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
#import data
import json
#system date & time
import datetime
date = datetime.datetime.now()
#email content
content = ""
# SERVER = 'smtp.gmail.com' PORT = 587
def send_email(SERVER,PORT,FROM,PASS,TO,msg):
    print("Initializing Email")
    server = smtplib.SMTP(SERVER,PORT)
    #server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM,PASS)
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print("Email Sent")
def email(SERVER,PORT,subject):
    print("Composing Email")
    FROM = '' #Assuming the sender is always the same, input your email here
    TO = [] #Assuming your
    PASS = ''
    try:
        with open('senders.json', 'r') as file:
            data = json.load(file)
            FROM = data["FROM"]
            PASS = data["PASS"]
    except FileNotFoundError:
        print("senders.json can't be found. Run the sender_data.py. Then, run this file")
        return
    except KeyError:
        print("Either FROM or PASS key is missing in senders.json. Running sender_data.py")
        return
    try:
        with open('receivers.json', 'r') as file:
            TO = json.load(file)  
    except FileNotFoundError:
        print("Receivers.json can't be found. Running receivers_data.py")
    msg = MIMEMultipart()
    msg['FROM'] = FROM
    msg['TO'] = ", ".join(TO)
    msg['Subject'] = subject + ' ' +str(date.day) + ' '+ str(date.month) + ' '+ str(date.year) + '\n'
    msg.attach(MIMEText(content,'html'))
    send_email(SERVER,PORT,FROM,PASS,TO,msg)

def main():
    # Get Content 
    global content
    subject = input("Subject: ")
    content = input("Input Message: ")
    content+=('<br>----------<br>')
    content+=('<br><br>End of Message')
    #Compose Email
    SERVER = 'smtp.gmail.com'
    PORT = 587
    email(SERVER,PORT,subject)


if __name__=='__main__':
    main()