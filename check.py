# check to see if the phone is connected to my router
def check_for_phone():
	import urllib.request
	import urllib.parse
	
	# username and password for my DLINK router
	username = 'readonly'
	password = '64eec07f11'
	router_address = '192.168.0.1'
	# MAC address of my phone
	phone_MAC_address = '00-11-45-b5-a8-96'
	
	params = urllib.parse.urlencode({'login_name' : username, 'login_pass' : password, 'login' : 'Log+in'})
	params = params.encode('utf-8')
	# login page
	f = urllib.request.urlopen("http://%s/login.cgi" % router_address, params)
	# connected wireless devices page
	f = urllib.request.urlopen("http://%s/lan.htm" % router_address)
	data = f.read().decode('utf-8')

	# search the HTML source for my MAC address, if it returns -1 it means it didn't find it
	if(data.find(phone_MAC_address) == -1):
	  return False
	else:
	  return True
