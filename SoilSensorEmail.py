import smtplib
from email.message import EmailMessage
import RPi.GPIO as GPIO
import time

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

from_email_addr = "207319913@qq.com"
from_email_pass = "btucoswgpburcaej"
to_email_addr = "iotyouxiang@qq.com"

def detect_send(channel):
        if GPIO.input(channel):
                print("Water Detected!")
		send_dont_need_water()
        else:
                print("No water Detected!")
		send_need_water()

def send_need_water()
	msg = EmailMessage()
	msg.set_content("MASTER!!!IM THIRSTY!!!!")
	msg['From'] = from_email_addr
	msg['To'] = to_email_addr
	msg['Subject'] = 'Need water'
	server = smtplib.SMTP('smtp.qq.com',587)
	server.starttls()
	server.login(from_email_addr,from_email_pass)
	server.send_message(msg)
	print('Email sent need water')
	server.quit()

def send_dont_need_water()
        msg = EmailMessage()
        msg.set_content("Hey,im not thirsty at all.")
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr
        msg['Subject'] = 'Dont need water'
        server = smtplib.SMTP('smtp.qq.com',587)
        server.starttls()
        server.login(from_email_addr,from_email_pass)
        server.send_message(msg)
        print('Email sent dont need water')
        server.quit()


# infinite loop
while True:
        time.sleep(0)
