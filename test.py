import subprocess

subprocess.Popen(['motion', '-l', 'log.txt', '-n'], stdin=None, stdout=None, stderr=None, close_fds=True, shell=True)
