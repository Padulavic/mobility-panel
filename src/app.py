from requests import get

import subprocess

import time

while(True):
	test = get("https://meowfacts.herokuapp.com/").json()
	output = test['data'][0]
	print(output);
	subprocess.Popen("./scrolling-text -f cherry-13-r.bdf --led-chain=4 %s" % output,shell=True)
	time.sleep(1000)
