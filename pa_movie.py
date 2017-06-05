# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import requests

url = 'https://movie.douban.com/top250?start=0&filter='
urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]


def get_doubai(url,data=None):
    #info = []
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)

    tiltes = soup.select('#content > div > div.article > ol > li > div > div.pic > a > img')
    imgs = soup.select('#content > div > div.article > ol > li > div > div.pic > a > img')
    ups = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p')
    scores  = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')
    commentss = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p.quote > span')
    #print(tiltes)


    for 标题,图片,评分,短语 in zip (tiltes,imgs,scores,commentss):
        data = {
            '标题':标题.get('alt'),
            '图片':图片.get('src'),
            #'演员阵容':演员阵容.get_text(),
            '评分':评分.get_text(),
            '短语':短语.get_text()
    }
        print(data)

for single_url in urls:
    get_doubai(single_url)
