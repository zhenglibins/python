# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
 
tops = []                                                        #创建空列表，用于储存词条
url = 'http://top.baidu.com/buzz?b=1&fr=20811' 
"""
http://top.baidu.com/buzz?b=1&fr=20811 百度实时热点
http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1_c513  百度今日热点
"""
r = requests.get(url, timeout=40)                                #获得url信息，设置40秒超时时间
r.raise_for_status()                                             #失败请求(非200响应)抛出异常
r.encoding = r.apparent_encoding                                 #根据内容分析出的编码方式，备选编码；
html = r.text                                                    #获得的HTML文本                                 
table = BeautifulSoup(html,"html.parser").find("table")          #对获得的文本进行html解析，查找<table>内的信息
for words in table.find_all("a"):                                #查找<table>内<a>的所有信息
    if words.string !='search' and words.string !='新闻' and words.string !='视频'and words.string !='图片':
        tops.append(words.string)                                #append() 方法用于在列表末尾添加新对象
    else:
        continue
for strs in tops:
    print(strs)