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

#Set the LastValue variable. Will compare to Current Hour Value
#lastValue = result.tm_hour + 8
seconds = time.time()
result =time.localtime(seconds)
startTime = 4
lastValue = startTime

def detect_send(channel):
	if GPIO.input(channel):
		print("No Water Detected!")
		send_need_water()
	else:
		print("Water Detected!")
		send_dont_need_water()

def send_need_water():
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

def send_dont_need_water():
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

while(True):
	seconds = time.time()
	result = time.localtime(seconds)
	Current_Value = result.tm_hour
	#print(str(Current_Value))
	#Compare Time to send email
	if(lastValue!=Current_Value):
		difference= Current_Value-lastValue
		if(difference >3):
			detect_send(channel)
			lastValue = Current_Value
