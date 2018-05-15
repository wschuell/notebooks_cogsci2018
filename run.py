import os
import sys
import binascii
import socket
import subprocess
import urllib
import random
import time
import webbrowser
import signal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for p in range(8888,9999):
	try:
		s.bind(('localhost', p))
		addr, port = s.getsockname()
		break
	except OSError:
		pass
s.close()

#token = binascii.hexlify(os.urandom(48))
token = ''.join(random.choice('0123456789abcdef') for _ in range(48))

os.environ['NOTEBOOKPORT'] = str(port)
os.environ['NOTEBOOKTOKEN'] = str(token)

os.environ['DOCKERTZ'] = time.tzname[time.daylight]

subprocess.call(['docker-compose','build'])

try:
	p = subprocess.Popen(['docker-compose','up'])
	time.sleep(3)
	webbrowser.open(str('http://localhost:'+str(port)+'/?token='+str(token)))
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	pass
finally:
	p.terminate()
	while p.poll() is None:
		time.sleep(0.1)