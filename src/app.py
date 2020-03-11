from requests import get
from subprocess import Popen
from time import sleep

while(True):
	payload = get("https://meowfacts.herokuapp.com/").json()
	output = payload['data'][0]
	print(output);
	proc = Popen("./static-text -f cherry-13-r.bdf --led-chain=4 %s" % output,shell=True)
	sleep(10)
	proc.kill()
