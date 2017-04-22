import urllib,urllib2
value = {'username':'261658232@qq.com', 'password':'slkdfjlke'}
data = urllib.urlencode(value)
url = "http://passport.csdn.net/account/login"
geturl = url + '?' + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()