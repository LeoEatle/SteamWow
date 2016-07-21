#this file use encoding: utf-8

import requests
from bs4 import BeautifulSoup
import urllib2, urllib

class UseBS:
    def get_money_for_game(self, steamid):
        '''Given a steamid(64) and return the total money cost for all the games'''

        steamid = str(steamid)
        #url = 'https://steamdb.info/calculator/%s/?cc=cn' %steamid
        url = "https://steamdb.info/calculator/76561198120356999/?cc=cn"
        headers = {  # 伪装为浏览器抓取
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        req = urllib2.Request(url, headers=headers)
        content = urllib2.urlopen(req).read()
        #好,现在已经可以成功拿到HTML数据了


        #现在开始寻找相关数据
        soup = BeautifulSoup(content, "html.parser")
        number_price_lowest = soup.select(".number-price-lowest").get_text()
        print "price", number_price_lowest


        #print content


if __name__ == '__main__':
    u = UseBS()
    u.get_money_for_game('LeoEatle')