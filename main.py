import subprocess
import check
import time

running = False
while True:
  # every minute check if phone exists
	status = check.check_for_phone()
	if(status == False):
	  print("Phone is not present")
	  # if it doesn't, run motion, only if it isn't running already
	  if(running == False):
	    print("Startiong motion")
	    subprocess.call(['/home/steve/motion/motion', '-c', 'motion.conf', '-l', 'log.txt'])
	    running = True
	else:
	  # if it does, kill motion
	  print("Phone is not present")
	  if(running == True):
      print("Killing motion")
      subprocess.call(['pkill', 'motion'])
      running = False
  print("Sleeping 60 seconds...")
	time.sleep(60)
