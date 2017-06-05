# _*_ coding:utf-8  _*_

from bs4 import BeautifulSoup
import  requests

headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-oa90-New_York_City_New_York.html#ATTRACTION_LIST'

mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
#print(soup)
imgs = soup.select('img[width="54"]')
for i in imgs:
    print(i.get('src'))
#print(imgs)
