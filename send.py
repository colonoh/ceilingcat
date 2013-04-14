#!/usr/bin/env python

import smtplib
import sys
import os
from email.mime.image import MIMEImage

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#pic = str(sys.argv[1])
#print('Pic =', pic)

msg = MIMEMultipart()

msg['Subject'] = 'Incomming image from webcam'
msg['From'] = 'stevewarner@cox.com'
msg['To'] = 'steve.j.warner@gmail.com'
#msg['To'] = '5182688230@vmobl.com'

#msg = MIMEText(":O")

# find the latest image in the images directory
image_dir = os.path.normpath('/home/steve/test_images/')
l = [(os.path.getmtime(os.path.join(image_dir, x)), x) for x in os.listdir(image_dir)]
l.sort()
latest = l[-1][1]
print('Latest file is', latest)
# check to make sure there is a latest file?

fp = open(os.path.join(image_dir, latest), 'rb')
#fp = open('/home/steve/test_images/01-20130203144639-00.jpg', 'rb')
#fp = open(pic, 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

s = smtplib.SMTP('smtp.cox.net')
s.send_message(msg)
s.quit()
