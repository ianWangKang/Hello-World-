# _*_  coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
#import time

url = 'https://knewone.com/discover?page='
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}

def get_knewone(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    imgs = soup.select('#wrapper > div > section > div > div.hits_group-things.clearfix > article > header > a > img')
    tltels = soup.select('#wrapper > div > section > div > div.hits_group-things.clearfix > article > section > h4 > a')
    links = soup.select('#wrapper > div > section > div > div.hits_group-things.clearfix > article > section > h4 > a')

    for 图片,标题,链接 in zip (imgs,tltels,links):
        data = {
            '图片':图片.get('src'),
            '标题':标题.get_text(),
            '链接':链接.get('href')
        }
        print(data)
def get_more_page(start,end):
    for one in range(start,end):
        get_knewone(url+str(one))
        #time.sleep(2)
get_more_page(1,100)