import urllib, urllib2
import os, re
import chardet

class Scrqpy_mode:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
        self.headers = {'User-Agent': user_agent}

    def opens(self, url):
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read()

    def wHTML(self, text, dir):
        code = chardet.detect(text)
        with open('%s/text.html' % dir,'w') as f:
            print code['encoding']
            f.write(text.decode(code['encoding', 'ignore']).encode('gbk', 'ignore'))
            

    def contentSave(self, data, dir):
        pattern = re.compile('<img src="(.*?community)/(.*?).([p|P|j|J|g|G][n|N|p|P|i|I][e|E|g|G|f|F][g|G]?)"', re.S)
        items = re.findall(pattern, data)
        imgurl = ''
        for item in items:
            local = os.path.join('%s/imgDir' % dir,'%s.%s' % (item[1], item[2]))
            url = item[0]+ '/' +item[1]+ '.' +item[2]
            urllib.urlretrieve(url, local)
            imgurl = item[0]
        text = re.sub(imgurl, 'imgDir',data)

        self.wHTML(text ,dir)


scrq = Scrqpy_mode()
pattern = re.compile('<div class="upJyBoxCon".*?class="ujTitle">.*?<a href="(.*?)".*?>(.*?)</a>.*?class="blackLink mt5".*?<span class="cf30">(.*?)</span>',re.S)
pattern2 = re.compile('<h1 class="workTitle f16 yh.*?<span>(.*?)</span>(.*?)<img.*?<div class="userName vm".*?<a.*?>(.*?)</a>.*?<div style="font-size.*?>(.*?)</div>.*?(<div class="workContent layout f16 c666".*?>.*?</div>).*?<span id="recommend_count1">(.*?)</span>.*?<div class="workNavRight">.*?<b>(.*?)</b>',re.S)
dir = 0
for int1 in range(1,20):
    url1 = 'http://www.zcool.com.cn/articles/0!0!0!0!0!200!1!'+str(int1)
    content = scrq.opens(url1)
    items = re.findall(pattern, content)
    for item in items:
        if int(item[2]) > 10000:
            dir += 1
            imgDir = '%s/imgDir' % dir
            if not os.path.exists(imgDir):
                os.makedirs(imgDir)
            print item[0],item[1],item[2]
            data2 = scrq.opens(item[0])
            items2 = re.findall(pattern2,data2)
            for item2 in items2:
                print item2[0], item2[1], item2[2], item2[3], item2[5]
                scrq.contentSave(item2[4], '%s' % dir)



