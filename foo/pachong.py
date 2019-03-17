# -*- coding: utf-8 -*-
import urllib
import re
import os

def analyHtml(address):
    pass
    page = urllib.request.urlopen(address)#打开网页
    htmlcode = page.read()
    return htmlcode.decode("utf-8")
def nullFunc():
    pass
reg = r'src="(.+?\.jpg)" pic_ext'
#print(reg);
#print('src="(.+?\.jpg)" pic_ext')
#print('src="(.+?\\.jpg)" pic_ext')
imgre = re.compile(reg)
imglist = imgre.findall(analyHtml('http://tieba.baidu.com/p/1753935195'))
path = '.\\images'; 
if not os.path.isdir(path):  
    os.makedirs(path)  
paths = path+'\\'      
x = 0;
for imgurl in imglist:
    while(os.path.exists(paths+str(x)+'.jpg')):
        x += 1;
    urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))
    print(imgurl)
    x += 1;


