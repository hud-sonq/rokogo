import time
import os
import linecache
import re
log = 'ngrok.log'
p = r'([a-zA-Z_][a-zA-Z_\d]*)=("[^"]*"|[^\s]+)'

def exec():
	os.system("ngrok start --all --log=stdout > ngrok.log &")
	time.sleep(1)

def parse_to_dict(s) -> dict:
	d = {}
	for k, v in re.findall(p, s):
		d[k] = v
	return d

def main():
	exec()
	info1 = linecache.getline(log, 8)
	url1 = parse_to_dict(info1)["url"]
	addr1 = parse_to_dict(info1)["addr"]
	info2 = linecache.getline(log, 9)
	url2 = parse_to_dict(info2)["url"]
	addr2 = parse_to_dict(info2)["addr"]
	print("tunnel " + url1 + " is exposed to " + addr1)
	print("tunnel " + url2 + " is exposed to " + addr2)
main()