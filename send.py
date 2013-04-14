#!/usr/bin/env python

import smtplib
import sys
import os
from email.mime.image import MIMEImage

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

images_dir = 'test_images'

msg = MIMEMultipart()

msg['Subject'] = 'Incomming image from webcam'
msg['From'] = 'stevewarner@cox.com'
msg['To'] = 'steve.j.warner@gmail.com'

# find the latest image in the images directory
image_dir = os.path.normpath(images_dir)
l = [(os.path.getmtime(os.path.join(image_dir, x)), x) for x in os.listdir(image_dir)]
l.sort()
latest = l[-1][1]
print('Latest file is', latest)
# check to make sure there is a latest file?

fp = open(os.path.join(image_dir, latest), 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

s = smtplib.SMTP('smtp.cox.net')
s.send_message(msg)
s.quit()
