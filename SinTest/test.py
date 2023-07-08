import smtplib
from dotenv import load_dotenv
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
my_email = os.environ.get("gmail")
my_password = os.environ.get("gmail_password")


sender_email = my_email
receiver_email = my_email
email_subject = "Daily Sine Bot Report"
log_file_path = "SinTest/stock_log.json"
with open(log_file_path, 'r') as log_file:
    file_contents = json.load(log_file)
    email_message = json.dumps(file_contents)

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = email_subject

# Attach the email body as a plain text MIME part
msg.attach(MIMEText(email_message, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 465
smtp_connection = smtplib.SMTP_SSL(smtp_server, smtp_port)

smtp_connection.login(my_email, my_password)

smtp_connection.sendmail(sender_email, receiver_email, msg.as_string())

smtp_connection.quit()