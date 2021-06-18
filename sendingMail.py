import smtplib
from email.message import EmailMessage

email_user = 'demo@example.com'
password = 'mailpass'
email_receiver = 'demo@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'Demo Subject'
msg['From'] = email_user
msg['To'] = email_receiver
msg.set_content("Demo Body ")

with smtplib.SMTP_SSL('mail.example.com', 465) as smtp:
	smtp.login(email_user, password)
	smtp.send_message(msg)
print('msg sent')