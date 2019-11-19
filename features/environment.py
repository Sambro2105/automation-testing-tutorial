import os
import time
from features.browser import Browser
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

screenshots_path = os.getcwd() + '\screenshots'

mail_content = 'Hello'
from_addr = 'urukhai1001@gmail.com'
password = 'fvcnthlfV1001'
to_addr = 'urugvai2105@gmail.com'
file_path = os.getcwd() + '\screenshots.zip'

def send_file_to_email():
    sender_address = 'urugvai2105@gmail.com'
    sender_pass = 'fynfyfyfhbde'
    receiver_address = 'urukhai1001@gmail.com'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Screenshots'
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = file_path
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

def before_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.close()
    shutil.make_archive(os.getcwd() + '\screenshots', 'zip', screenshots_path)
    send_file_to_email()
    if os.path.isdir(screenshots_path):
        shutil.rmtree(screenshots_path)
    if os.path.isfile(file_path):
        os.remove(file_path)
