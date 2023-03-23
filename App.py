#!/usr/bin/evn python3
import requests
r = requests.get('https://www.google.com')
if r.status_code == 200:
	print('okkkk')
else:
	print ('nooo')