import re
import requests
import json
import urllib.request
import urllib.error
import os
import sys

minimumsize = 10
print('fetching msg from %s \n' % sys.argv[1])
url = re.sub('#/', '', sys.argv[1]) # 将sys.argv[1]的字符串去掉#/后赋值给url
r = requests.get(url) # 获得一个带有url参数的Response
contents = r.text # 获取页面内容
res = r'<ul class="f-hide">(.*?)</ul>' # 样式类为class='f-hide'的ul标签
mm = re.findall(res, contents, re.S | re.M) # 在contents中匹配res的内容
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__)) # 绝对路径
if(mm):
    contents = mm[0]
else:
    print('Can not fetch information form URL. Please make sure the URL is right. \n')
    os._exit(0)
# 
res = r'<li><a .*?>(.*?)</a></li>'
mm = re.findall(res, contents, re.S | re.M)

# 筛选内容，找到class='f-hide'的ul中，li-a中的内容信息
# 也就是获取歌曲列表
for value in mm:
    url = 'http://sug.music.baidu.com/info/suggestion'
    payload = {'word': value, 'version': '2', 'from': '0'}
    print(value)

    r = requests.get(url, params=payload)
    # 获取了一个参数为url和payload的Response对象
    contents = r.text
    d = json.loads(contents, encoding='utf-8')
    # 获取内容，进行编码
    if d is not None and 'data' not in d:
        continue # 判断d不为None 并且 没有'data'这个键，则跳出本次循环
    songid = d['data']['song'][0]['songid']
    print('find songid: %s' % songid)

    url = 'http://music.baidu.com/data/music/fmlink'
    payload = {'songIds': songid, 'type': 'flac'}
    r = requests.get(url, params=payload)
    contents = r.text
    d = json.loads(contents, encoding='utf-8')
    if('data' not in d) or d['data'] == '':
        continue
    songlink = d['data']['songList'][0]['songLink']
    print('find songlink: ')
    if(len(songlink) < 10):
        print('\tdo not have flac\n')
        continue
    print(songlink)

    songdir = 'songs_dir'
    if not os.path.exists(songdir):
        os.makedirs(songdir)

    songname = d['data']['songList'][0]['songName']
    artistName = d['data']['songList'][0]['artistName']
    filename = ('%s/%s/%s-%s.flac' % (CURRENT_PATH, songdir, songname, artistName))

    f = urllib.request.urlopen(songlink)
    headers = requests.head(songlink).headers
    size = round(int(headers['Content-Length'])/(1024 ** 2),2)

    #Download unfinished Flacs again.
    if not os.path.isfile(filename) or os.path.getsize(filename) < minimumsize:
        print('%s is downloading now ......\n\n' % songname)
        if size >= minimumsize:
            with open(filename, 'wb') as code:
                code.write(f.read())
        else:
            print('the size of %s (%r Mb) is less than 10 Mb,skipping' % (filename,size))
    else:
        print('%s is already downloaded. finding next song...\n\n' % songname)


print('\n===================================================================\n')
print("Download finish!\nSongs' directory is %s/songs_dir" % os.getcwd())
