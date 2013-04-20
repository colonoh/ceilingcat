import subprocess
from check import check_for_phone
import time

running = False
while True:
  # every minute check if phone exists
  if(check_for_phone() == False):
    print("Phone is NOT connected to router")
    
    # if it doesn't, run motion, only if it isn't running already
    if(running == False):
      print("Startiong motion")
      subprocess.call(['/home/steve/motion/motion', '-c', 'motion.conf', '-l', 'log.txt'])
      running = True
  
  else:
    # if phone is present, kill motion
    print("Phone is connected to router")
    if(running == True):
      print("Killing motion")
      subprocess.call(['pkill', 'motion'])
      running = False
  print("Sleeping 60 seconds...")
  time.sleep(60)
