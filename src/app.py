from requests import get
from subprocess import Popen
from time import sleep
import signal
import os

while(True):
	payload = get("https://meowfacts.herokuapp.com/").json()
	output = payload['data'][0]
	print(output);
	proc = Popen("./scripts/scrolling-text-example -f \
		 fonts/10x20.bdf \
		 --led-chain=4 \
	 	 -y 6 \
		 -C 115,0,230 \
		 %s" % output,shell=True)
	#proc = Popen(["./scripts/scrolling-text-example -f fonts/10x20.bdf --led-chain=4 -y 6 -C 115,0,230 %s" % output])
	sleep(20)
	#proc.send_signal(signal.SIGINT)
	#proc.kill()
	#os.kill(os.getpgid(proc.pid), signal.SIGTERM)
	Popen(["pkill", "-P", str(proc.pid)])
