# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
sz_bnb_info = xiaozhu['sz_bnb_info']

# url = 'http://sz.xiaozhu.com/search-duanzufang-p0-0/'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
# titles = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
# prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
#
# for title,price in zip (titles,prices):
#     data = {
#         'title':title.get_text(),
#         'price':int(price.get_text())
#     }
#     sz_bnb_info.insert_one(data)
# print('Done')

def get_page_within(pages):
    for page_num in range(1,pages+1):
        wb_data = requests.get('http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(page_num))
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
        prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')

        for title,price in zip (titles,prices):
            data = {
            'title':title.get_text(),
            'price':int(price.get_text())
            }
            sz_bnb_info.insert_one(data)
    print('Done')

get_page_within(50)

for i in sz_bnb_info.find():
    if i['price'] >= 10:
        print(i)
