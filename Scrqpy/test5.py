import urllib,urllib2,re


int1 = 1
data = ''
try:
    str1 = '0!0!0!0!0!200!1!'+str(int1)
    url = 'http://www.zcool.com.cn/articles/'+str1
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    headers = {'User-Agent':user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
except urllib2.URLError,e:
    print e

pattern = re.compile('<div class="upJyBoxCon".*?class="ujTitle">.*?<a href="(.*?)".*?>(.*?)</a>',re.S)
items = re.findall(pattern, data)
for item in items:
    print item[0],item[1]