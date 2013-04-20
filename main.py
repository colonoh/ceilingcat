import subprocess
import check
import time

# THIS IS SHIT

running = False
while True:
	# every minute
	# check if phone exists
	status = check.check_for_phone()
	print('Status is', status)
	if(status == 0):
	  print("PHONE IS NOT PRESENT")
	  # if it doesn't, run motion
	  # ONLY IF IT ISN'T RUNNING ALREADY
	  if(running == False):
	    #p = subprocess.call(['motion', '-n'])
	    #p = subprocess.call(['motion', '-l', 'log.txt'])
	    subprocess.call(['/home/steve/motion/motion', '-c', 'motion.conf', '-l', 'log.txt'])
            # TODO: ADD -l log.txt, doesn't seem to send e-mail unless -n (non-daemon mode) is used, but then gets stuck in following process
	    running = True
	else:
	  # if it does, kill kill motion
	  # get motion id and kill 
	  print("KILLING MOTION")
	  subprocess.call(['pkill', 'motion'])
	  running = False
	print("Sleeping 60 seconds...")
	time.sleep(10)



