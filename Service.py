#this file use encoding: utf-8

import requests
from SteamBase import SteamAPI
"""
This Service use the Steam API Key: C049B2E299BF41A736C43E6F8C45F5DE
Domain Name: leoeatle.com
Acquired by: LeoEatle
"""


class Service(SteamAPI):
    def __init__(self,num=None):
        """
        args:
        num -- number of games to query per call. The default 150 should work in most cases.

        """
        self.num = 150 if num is None else num
        self.appids_to_names, self.names_to_appids = None, None

    def get_money_for_game(self, steamid):
        '''Given a steamid(64) and return the total money cost for all the games'''
        #At first, intitialize the price adder
        initial_price = 0
        final_price = 0


        steamid = str(steamid)
        print 'steamid', steamid
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=C049B2E299BF41A736C43E6F8C45F5DE&steamid=%s&format=json" %steamid
        url_info = requests.get(url).json()
        #print url_info

        #get all the games
        allgames = url_info['response']['games']
        appid = ""
        for game in allgames:
            appid = appid + "," + str((game["appid"]))
        appid = appid[1:]
        #CC is the money type
        url_for_app = "http://store.steampowered.com/api/appdetails/?appids=%s&cc=CN&l=english&v=1&filters=price_overview" %appid
        url_app_info = requests.get(url_for_app).json()

        for game in url_app_info:

            if url_app_info[game]['success'] and url_app_info[game]['data']:
                price_overview = url_app_info[game]['data']['price_overview']
                if price_overview['initial'] != 0:
                    #print "initial_price", price_overview['initial']
                    #print "final_price",
                    initial_price += price_overview['initial']
                    final_price += price_overview['final']


        #print "url_app_info", url_app_info

        print appid
        return initial_price, final_price




if __name__ == '__main__':
    s = Service()
    initial_price, final_price = s.get_money_for_game (76561198120356999)
    print "initial_price", initial_price
    print "final_price", final_price
