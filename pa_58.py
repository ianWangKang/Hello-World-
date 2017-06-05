# _*_ coding-utf-8 _*_

import requests
from  bs4  import BeautifulSoup

url = 'http://zhuanzhuan.58.com/detail/803242911106727938z.shtml'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}


def get_links_from(url):
    urls = []
    list_view = 'http://sz.58.com/pbdn/'
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select(' td.t  a.t'):
        urls.append(link.get('href').split('?')[0])
    #return urls
    print(urls)



def get_item_info(urls):
    wb_data = requests.get(urls)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)

    title = soup.select('div span.crb_i  a')
    price = soup.select(' div span.price_now i')
    palce = soup.select('div.palce_li span i')
    view = soup.select('div span.look_time')

    data = {
        'title':title[0].text,
        'price':price[0].text,
        'palce':palce[0].text,
        'view':view[0].text
    }

    print(data)

get_item_info()

#get_links_from(url)


