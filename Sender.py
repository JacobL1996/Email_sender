import email
import smtplib
import ssl
import os
import time

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email():
	port = 465 #use this for SSL
	#can import getpass and use .getpass() to no see input
	password = "CowP00p$" #input("type in your password and press enter: ")

	#critical for sending emails
	subject = "An email sent with an attachment with Python"
	body = "This email should be an image of a cow."
	smp_server = "smtp.gmail.com"
	sender_email = "aemtamu@gmail.com"
	receiver_email = "aemtamu@gmail.com"

	#TODO: get image from camera of Pi
	file_name = "cow.jpg"

	#open image file
	img_data = open(file_name, 'rb').read()
	print("opened file")

	#create a message with multiple parts
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject

	image = MIMEImage(img_data, name=os.path.basename(file_name))
	message.attach(image)
	print("attached file")

	message.attach(MIMEText(body, "plain"))
	#create a secure SSL context
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message.as_string())
	

count = 0
while(count < 5):
	send_email()
	time.sleep(30)
	count += 1