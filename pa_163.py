# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'http://1.163.com/list/0-0-1-1.html'
urls = ['http://1.163.com/list/0-0-1-{}.html'.format(str(i)) for i in range(2,6)]
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}

def get_163(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')

    titles = soup.select('#goodsList > li > div > p.w-goods-title.f-txtabb > a')
    prices    = soup.select('#goodsList > li > div > p.w-goods-price')
    numbers = soup.select('#goodsList > li > div > div.w-progressBar > ul > li.w-progressBar-txt-l > p > b')
    #print(prices)


    for 名称,总需人次,已参与人次 in zip (titles,prices,numbers):
        data ={
            '名称':名称.get_text(),
            '总需人次':总需人次.get_text(),
            '已参与人次':已参与人次.get_text()
        }
        print(data)
for single_url in urls:
    get_163(single_url)