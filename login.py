import urllib, urllib2, cookielib

username = 'alortiz'
password = 'F4nd4ng006!'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
opener.open('https://easya.t-systems.es/auth/login', login_data)
resp = opener.open('https://easya.t-systems.es/index/getlink/ID/8')
print resp.read()

