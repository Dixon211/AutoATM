import smtplib
from dotenv import load_dotenv
import os
import json

load_dotenv()
my_email = os.environ.get("gmail")
my_password = os.environ.get("gmail_password")


sender_email = my_email
receiver_email = my_email
email_subject = "Daily Sine Bot Report"
log_file_path = "./stock_log.json"
with open(log_file_path, 'r') as log_file:
    file_contents = json.load(log_file_path)
    email_message = file_contents

smtp_server = 'smtp.gmail.com'
smtp_port = 465
smtp_connection = smtplib.SMTP_SSL(smtp_server, smtp_port)

smtp_connection.login(my_email, my_password)

smtp_connection.sendmail(sender_email, receiver_email, email_message)

