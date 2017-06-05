# _*_ coding:utf-8 _*_

import string
import re
import urllib2

class doubanspider(object):
    def __init__(self):
        self.page = 1
        self.cur_url = "https://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print "豆瓣电影爬虫准备就绪,准备爬取数据。。。"

    def get_page(self,cur_page):
        """

        根据当前页码爬取页面HTML

         Args:
             cur_page:表示当前所抓取的网页页码

         Returns:
             返回抓取到整个页面的HTML(unicode编码)

         Raises:
             URLError:url引发的异常
        """

        url = self.cur_url
        try:
            my_page = urllib2.urlopen(url.format(page = (cur_page - 1) * 25)).read().decode("utf-8")
        except urllib2.URLError, e :
            if hasattr(e,"code"):
                print "The server couldn't fulfill the request."
                print "Error code :%s" % e.code
            elif hasattr(e,"reason"):
                print "We failed to reach a server.please check your url and read the Reason"
                print  "Reason: %s" % e.reason
        return my_page
    def find_title(self,my_page):
        """

        通过返回的整个页面HTML,正则匹配前100的电影名称

        Args:
            my_page:传入页面的HTML文本用于正则匹配
        """
        temp_data = []
        movie_items = re.findall(r'<span.*?class="titel">(.*?)</span>',my_page,re.S)
        for index,item in enumerate(movie_items):
            if item.find("&nbsp") == -1:
                temp_data.append("Top" + str(self._top_num) + " " + item)
                self._top_num += 1
        self.datas.extend(temp_data)
    def start_spider(self):
        """

        爬虫入口,并控制爬虫抓取页面的范围
        """


        while self.page <= 4:
            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page += 1

def main():
    print """
        ###########################
        一个简单的豆瓣电影前100爬虫
        date: 2016-11-22
        ###########################
"""
    my_spider = doubanspider()
    my_spider.start_spider()
    for itme in my_spider.datas:
        print itme
    print "豆瓣爬虫爬取结束。。。"

if  __name__ == '__main__':
    main()
