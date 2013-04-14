def check_for_phone():
	import urllib.request
	import urllib.parse
	
	# user-set parameters
	username = 'readonly'
	password = '64eec07f11'
	router = '192.168.0.1'
	target = '00-11-94-ba-49-3c'
	
	params = urllib.parse.urlencode({'login_name' : username, 'login_pass' : password, 'login' : 'Log+in'})
	params = params.encode('utf-8')
	
	f = urllib.request.urlopen("http://%s/login.cgi" % router, params)
	
	#params = 0
	#params = params.encode('utf-8')
			
	#f = urllib.request.urlopen("http://%s/st_wireless.htm" % router, params)
	f = urllib.request.urlopen("http://%s/st_wireless.htm" % router)
	
	data = f.read().decode('utf-8')
	
	result = data.find(target)
	
	# if find() doesn't find what it's looking for, it returns -1
	if(result == -1):
	  result = 0
	else:
	  result = 1
	
	#print(result)
	return result
