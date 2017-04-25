# -*- coding:utf-8 -*-
import urllib, urllib2, re

page = 2
url = 'http://www.qidian.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
#connection = 'keep-alive'
#cacheControl = 'max-age=0'
#acceptLanguage = 'zh-CN,zh;q=0.8'
#accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
#acceptEncoding = 'gzip, deflate, sdch'
#cookie = '_qqq_uuid_="2|1:0|10:1493085825|10:_qqq_uuid_|56:Yzg2NmM4NDliOTIzZWEwZjE4MjkxYmVkY2E3NjYzNDYyYWU2OTdjZA==|1afc7b062f20f27a7118fd0f0302f23b2376511e3d2fffb081c618a21caf581a"; _xsrf=2|be69cba2|41176ab1620ab72d74458a6842eb760f|1493087279; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1493086297,1493087749; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1493087749; _ga=GA1.2.2079207251.1493086297; _gat=1'
#upgradeInsecureRequests = '1'
headers = {'User_Agent':user_agent}#'Accept-Encoding':acceptEncoding,'Accept': accept, 'Accept-Language': acceptLanguage,'Cache-Control':cacheControl, 'Connection' : connection , 'Cookie': cookie , 'Upgrade-Insecure-Requests': upgradeInsecureRequests ,
data = ''
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read().decode('utf-8')
    print data
except urllib2.URLError, e:
    if hasattr(a, 'code'):
        print e.code
    if hasattr(a, 'reason'):
        print e.reason
pattern = re.compile('<a.*?class=name .*?>(.*?)</a>', re.S)
items = re.findall(pattern, data)
print items
for item in items:
    print item# -*- coding:utf-8 -*-
import urllib, urllib2, re

page = 2
url = 'http://www.qidian.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
#connection = 'keep-alive'
#cacheControl = 'max-age=0'
#acceptLanguage = 'zh-CN,zh;q=0.8'
#accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
#acceptEncoding = 'gzip, deflate, sdch'
#cookie = '_qqq_uuid_="2|1:0|10:1493085825|10:_qqq_uuid_|56:Yzg2NmM4NDliOTIzZWEwZjE4MjkxYmVkY2E3NjYzNDYyYWU2OTdjZA==|1afc7b062f20f27a7118fd0f0302f23b2376511e3d2fffb081c618a21caf581a"; _xsrf=2|be69cba2|41176ab1620ab72d74458a6842eb760f|1493087279; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1493086297,1493087749; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1493087749; _ga=GA1.2.2079207251.1493086297; _gat=1'
#upgradeInsecureRequests = '1'
headers = {'User_Agent':user_agent}#'Accept-Encoding':acceptEncoding,'Accept': accept, 'Accept-Language': acceptLanguage,'Cache-Control':cacheControl, 'Connection' : connection , 'Cookie': cookie , 'Upgrade-Insecure-Requests': upgradeInsecureRequests ,
data = ''
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read().decode('utf-8')
    print data
except urllib2.URLError, e:
    if hasattr(a, 'code'):
        print e.code
    if hasattr(a, 'reason'):
        print e.reason
pattern = re.compile('<a.*?class=name .*?>(.*?)</a>', re.S)
items = re.findall(pattern, data)
print items
for item in items:
    print item