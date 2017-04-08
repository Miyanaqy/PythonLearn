from urllib import request
from bs4 import BeautifulSoup

def fatch_xml(url):
    req = request.Request(url)
    with request.urlopen(req) as page:
        data = page.read()
        soup = BeautifulSoup(data, 'html.parser')
        count = 0
        for i in soup.select('div[class="D(ib) Va(m) W(1/4)"]'):
            count = count + 1

        for j in range(count):
            print('星期:', soup.select('div[class="D(ib) Va(m) W(1/4)"]') [j].get_text())
            print('天气:', soup.select('span[class="D(ib) Va(m) W(1/4) Ta(c)"] > img') [j]['title'])
            q = soup.select('span[class="D(ib) Va(m) W(1/4) Ta(end)"]') [j].get_text()
            print('温度:', 'high:%sF' % (a[0:3],a[3:6]))
            print('-' * 30)

    fatch_xml('https://www.yahoo.com/news/weather/china/beijing/beijing-2151330')
