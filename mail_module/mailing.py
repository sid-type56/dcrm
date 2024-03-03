import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(sender_email, recipient_email, subject, body):
    smtp_host = os.getenv("MAIL_SERVER")   # Replace with your SMTP server host
    smtp_port = os.getenv("MAIL_PORT")   # Replace with your SMTP server port
    smtp_username = os.getenv("MAIL_USERNAME")   # Replace with your SMTP username
    smtp_password = os.getenv("MAIL_PASSWORD")   # Replace with your SMTP password

    # Create a MIME message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()  # Enable encryption
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


# Example usage
send_email(os.getenv("MAIL_SERVER"), os.getenv("MAIL_RECIPIENT"), 'Test Email', 'This is a test email.')
