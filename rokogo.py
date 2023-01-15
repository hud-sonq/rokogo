import time
import os
import linecache
import re
import requests

log = 'ngrok.log'
p = r'([a-zA-Z_][a-zA-Z_\d]*)=("[^"]*"|[^\s]+)'
discord_url = "" #Optional. Place webhook here to send as a channel msg

def exec():
	os.system("ngrok start --all --log=stdout > ngrok.log &")
	time.sleep(1)

def parse_to_dict(s) -> dict:
	d = {}
	for k, v in re.findall(p, s):
		d[k] = v
	return d

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
	exec()
	#first app
	info1 = linecache.getline(log, 8)
	url1 = parse_to_dict(info1)["url"]
	addr1 = parse_to_dict(info1)["addr"]
	#second app
	info2 = linecache.getline(log, 9)
	url2 = parse_to_dict(info2)["url"]
	addr2 = parse_to_dict(info2)["addr"]
	#message vars 
	status1 = "Tunnel " + url1 + " is exposed to " + addr1
	status2 = "Tunnel " + url2 + " is exposed to " + addr2
	#integration if webhook exists
	if discord_url != "":
		rokbot(status1, status2)
main()