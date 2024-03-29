from email.message import EmailMessage
from password import password # create a file called password.py
import ssl
import smtplib

email_sender = "" # Sender email address
email_password = password
email_receiver = "" # Receiver email address

subject = "Just form python project - emailsender"
body = """
Write some text message for you, just test
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
