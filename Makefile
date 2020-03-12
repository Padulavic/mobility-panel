run:
	 python src/app.py

config:
	echo "requires SU credentials and internet connection"
	apt-get install python-pip
	pip install requests
	
