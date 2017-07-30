#!/usr/bin/python3.4
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
import smtplib
import os
import socket
HOSTNAME = socket.gethostname()
SERVER = "localhost"
FROM = "alerts@" + HOSTNAME
TO = "vipin@vipinm.com"
threshold = 5

def send_email(message, email):
	server = smtplib.SMTP(SERVER)
	server.sendmail(FROM, TO, message)
	server.quit()
disk_list = []
df = Popen(["df", "-h"], stdout=PIPE).communicate()[0]
lines = df.splitlines()[1:]
for line in lines:
	splitline = line.decode().split()
	partition = splitline[5]
	percent = int(splitline[4][:-1])
	if percent > threshold:
		disk_list.append(partition)
message = "CRITICAL: Disk partitions %s are using %s%% of size" %(disk_list, percent)
send_email(message, TO)
