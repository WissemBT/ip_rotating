import requests

proxies_list = open("rotating_proxies_list.txt","r").read().strip().split("\n")

VALID_STAT = [200,301,302,307,404]
def get(url,proxy):
	try:
		response=requests.get(url,proxies={'http': f"http://{proxy}"},timeout=30)
		if response.status_code in VALID_STAT:
			print(response.status_code,response.text)
	except Exception as e:
		print(e)
def check_proxies():
	for proxy in proxies_list:
		get("http://ident.me/",proxy)

check_proxies()
