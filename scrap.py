import requests

proxies_list = open("rotating_proxies_list.txt","r").read().strip().split("\n")

proxies = set(proxies_list)
good_proxy = set()
bad_proxy = set()

VALID_STAT = [200,301,302,307,404]
def get(url,proxy):
	try:
		response=requests.get(url,proxies={'http': f"http://{proxy}"},timeout=30)
		if response.status_code in VALID_STAT:
			#print(response.status_code,response.text)
			set_good(proxy)
		else:
			set_bad(proxy)
	except Exception as e:
		set_bad(proxy)
def check_proxies():
	for proxy in list(proxies):
		get("http://ident.me/",proxy)

def reset_proxy(proxy):
	proxies.add(proxy)
	good_proxy.discard(proxy)
	bad_proxy.discard(proxy)
def set_good(proxy):
	proxies.discard(proxy)
	good_proxy.add(proxy)
	bad_proxy.discard(proxy)
def set_bad(proxy):
	proxies.discard(proxy)
	good_proxy.discard(proxy)
	bad_proxy.add(proxy)
check_proxies()

print("not used : ", proxies)
print("good proxies : ", good_proxy)
print("bad proxies : ",bad_proxy)
