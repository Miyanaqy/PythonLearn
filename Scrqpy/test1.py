import urllib,urllib2

value = {"username":"1016903103@qq.com","password":"password"}
data = urllib.urlencode(value)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()