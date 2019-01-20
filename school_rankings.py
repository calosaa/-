# -*- coding: utf-8 -*-
"""

@author: Administrator
"""
import requests
from lxml import etree
import pymongo
url='https://www.dxsbb.com/news/5463.html'
headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
clinet=pymongo.MongoClient(host='localhost',port=27017)
db=clinet.school_rankings
collection=db.schools

def getHTML(url):
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text

def parse_html(text):
    html=etree.HTML(text)
    index=html.xpath('//table//td[@width="69"]/text()')
    name=html.xpath('//table//td[@width="160"]/text()')
    grade=html.xpath('//table//td[@width="85"]/text()')
    star_ratings=html.xpath('//table//td[@width="84"]/text()')
    education_level=html.xpath('//table//td[@width="230"]/text()')
    length=len(index)
    for i in range(0,length-1):
        one_list={'index':index[i],'name':name[i],'grade':grade[i],'start_ratings':star_ratings[i],'education_level':education_level[i]}
        result=collection.insert(one_list)
    return result

def main(url):
    html=getHTML(url)
    result_db=parse_html(html)
    print(result_db)

if __name__=='__main__':
    main(url)
    
