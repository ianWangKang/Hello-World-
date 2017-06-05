# _*_ coding:utf-8 _*_

from bs4 import  BeautifulSoup
import requests

url = 'http://bj.xiaozhu.com/'
urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(2,50)]




def get_xiaozhu(url,data=None):
    #info = []
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')


    titles = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > a > span')
    imgs = soup.select('#page_list > ul > li > a > img')
    prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
    addesss = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > div > em')
    landlord_imgs = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_img > a > img')

#print(landlord_imgs)


    for 标题,图片,每晚价格,地址,房东图片 in zip(titles,imgs,prices,addesss,landlord_imgs):
        data = {
            '标题':标题.get_text(),
            '图片':图片.get('src'),
            '每晚价格':每晚价格.get_text(),
            '地址':地址.get_text(),
            '房东图片':房东图片.get('lazy_src')
        }
    #info.append(data)
        print(data)

for single_url in urls:
    get_xiaozhu(single_url)





'''
    for title,img,price,addess,landlord_img in zip(titles,imgs,prices,addesss,landlord_imgs):
        data = {
            'title':title.get_text(),
            'img':img.get('src'),
            'price':price.get_text(),
            'addess':addess.get_text(),
            'landlord_img':landlord_img.get('lazy_src')
        }
        print(data)
'''


