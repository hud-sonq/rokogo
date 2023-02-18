import time
import os
import linecache
import re
import requests
import yaml
from pathlib import *


#add loop to scan for ports wanted
#and scan for app type (tcp, udp, etc)
#then implement those vars into the script
def makeconfig():
	apps = []
	app_number = int(input("How many apps to deploy? : "))
	anum = 1
	while(anum <= app_number):
		app_name = input("Enter a name for app " + str(anum) + ": ")
		app_port = int(input("Enter a port for app " + str(anum) + ": "))
		app_type = input("Enter a tunnel type (tcp, udp, etc) : ")
		apps.extend((str(app_name), str(app_port), str(app_type)))
		anum += 1
	Path("ngrok.yml").touch()
	data = {
    'version': '"2"',
    'authtoken':'foo',
    'tunnels': {apps[0]: {'addr': apps[1], 'proto': apps[2]}}
    }
	with open(f'ngrok.yml', 'w') as f:
		yaml.dump(data, f, sort_keys=False)
	

log = 'ngrok.log'
p = r'([a-zA-Z_][a-zA-Z_\d]*)=("[^"]*"|[^\s]+)'
discord_url = "" #Webhook here
#Start ngrok and log
def exec():
	os.system("ngrok start --all --log=stdout > ngrok.log &")
	time.sleep(1)
#Dict conversion
def parse_to_dict(s) -> dict:
	d = {}
	for k, v in re.findall(p, s):
		d[k] = v
	return d
#Discord integration
def rokbot(x, y):
	data = { 
		"content" : x + "\n" + y,
		"username" : "RokBot"
	}
	result = requests.post(discord_url, json = data)
	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print("Payload delivered successfully, code {}.".format(result.status_code))

def main():
	makeconfig()
	
	# exec()
	# #First app
	# info1 = linecache.getline(log, 8)
	# url1 = parse_to_dict(info1)["url"]
	# addr1 = parse_to_dict(info1)["addr"]
	# #Second app
	# info2 = linecache.getline(log, 9)
	# url2 = parse_to_dict(info2)["url"]
	# addr2 = parse_to_dict(info2)["addr"]
	# #Message vars 
	# status1 = "Tunnel " + url1 + " is exposed to " + addr1
	# status2 = "Tunnel " + url2 + " is exposed to " + addr2
	# #Integration if webhook exists
	# if discord_url != "":
	# 	rokbot(status1, status2)
main()