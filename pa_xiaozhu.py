# _*_  coding:utf-8 _*_

import  requests
from bs4 import BeautifulSoup

url = 'http://bj.xiaozhu.com/fangzi/5568044113.html'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
#print(soup)

titles = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em ')
imgs = soup.select('#curBigImage')
addresss = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')[0].text
rents = soup.select('#pricePart > div.day_l > span')
landlord_imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
landlord_names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
genders = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')[0].get('class')[0]
print(addresss,genders,titles)


def print_genders(class_name):
    if class_name == 'member_boy_ico1':
        return '女'
    if class_name == 'member_boy_ico':
        return '男'

for title,img,address,rent,landlord_img,landlord_name,gender in zip (titles,imgs,addresss,rents,landlord_imgs,landlord_names,genders):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'address':addresss,
        'rent':rent.get_text(),
        'landlord_img':landlord_img.get('src'),
        'landlord_name':landlord_name.get_text(),
        'gender':print_genders(genders)
    }
    print(data)
