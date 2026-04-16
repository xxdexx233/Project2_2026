import smtplib
from email.message import EmailMessage

from_email_addr = "207319913@qq.com"
from_email_pass = "btucoswgpburcaej"
to_email_addr = "iotyouxiang@qq.com"

msg = EmailMessage()
msg.set_content("Hello from Respberry PI")
msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.qq.com',587)
server.starttls()
server.login(from_email_addr,from_email_pass)
server.send_message(msg)
print('Email sent')
server.quit()
