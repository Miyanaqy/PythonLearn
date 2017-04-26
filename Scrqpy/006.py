import urllib, urllib2, re, os


int1 = 1
data = ''
try:
    url = 'http://www.zcool.com.cn/article/ZNDkwNDQw.html'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    headers = {'User-Agent':user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read().decode('utf-8')
except urllib2.URLError,e:
    print e

pattern = re.compile('<h1 class="workTitle f16 yh.*?<span>(.*?)</span>(.*?)<img.*?<div class="userName vm".*?<a.*?>(.*?)</a>.*?<div style="font-size.*?>(.*?)</div>.*?(<div class="workContent layout f16 c666".*?>.*?</div>).*?<span id="recommend_count1">(.*?)</span>.*?<div class="workNavRight">.*?<b>(.*?)</b>',re.S)
items = re.findall(pattern, data)
print items
imgDir = '%s/imgDir' % int1
if not os.path.exists(imgDir):
    os.makedirs(imgDir)

web_dir = ''
for item in items:
    pattern2 = re.compile('<img src="(.*?community)/(.*?).jpg" ', re.S)
    print item[4]
    items2 = re.findall(pattern2, item[4])
    for item2 in items2:
        print item2[0],item2[1]
        imgurl = item2[0] +'/'+ item2[1] + '.jpg'
        web_dir = item2[0]
        local = os.path.join(imgDir, '%s.jpg' % item2[1])
        print 'http:'+imgurl, 'dir:'+local
        urllib.urlretrieve(imgurl, local)
    text = re.sub(web_dir, imgDir, item[4])
    with open('%s/text.html' % int1, 'wb') as f:
        f.write(text.encode('utf-8'))

    print item[0],item[1],item[2],item[3],item[4],item[5],item[6]