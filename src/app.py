from requests import get
from subprocess import Popen
from time import sleep

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
	sleep(1000)
	proc.terminate()
