import json
import urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket # socket.setdefaulttimeout(5.0) -> You can control the delay before socket.timeout is raised by calling socket.setdefaulttimeout(5.0).

class Tradesatoshi:


    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}


    def initUrl(self,sigla):
        global buyTradeApi,sellTradeApi
        # --- TRADESATOSHI --- **{"success":true,"message":null,"result":{"buy":[{"quantity":100.00000000,"rate":0.00000021},{"quantity":600.00000000,"rate":0.00000016}],"sell":[]}} **
        urlTrade = "https://tradesatoshi.com/api/public/"
        buyTradeApi = urlTrade + "getorderbook?market="+sigla+"_BTC&type=buy&depth=2"
        sellTradeApi = urlTrade + "getorderbook?market="+sigla +"_BTC&type=sell&depth=2"



    socket.setdefaulttimeout(5.0)
    def caricaJSON(self,url):
        request = None
        response = None
        try:
            request = Request(url, headers=self.hdr)
            response = json.loads(urlopen(request,timeout=5.0).read())
        except (ValueError,urllib2.HTTPError) as error:
            print("#####################################")
            print("**ERROR**, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Check -> " + url)
            print("Response: " + str(response))
            print(urlopen(request).read())
            print("#####################################")
            pass
        except IOError as err:
            print('timeout')
            print(err)
        else:
            return response


    def tradeListaBuy(self,sigla):
        global buyTradeApi, dato
        print ("######## TRADESAT BUY ############")
        nDati = 1
        try:
            response = self.caricaJSON(buyTradeApi)
            #nDati = len(response["result"]["buy"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + buyTradeApi)
            print(response)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["result"]["buy"][a]["quantity"]))
                    dato.append(float(response["result"]["buy"][a]["rate"]))
                    dato.append("Tradesat Buy")
                    dato.append(sigla)
                return dato
            except (IndexError,TypeError) as error:
                print("#####################################")
                print("**ERROR1**")
                print response
                print("Something wrong, probably the market haven't " + sigla)
                print(error)
                print("#####################################")
                #// ne
                return []



    def tradeListaSell(self,sigla):
        global sellTradeApi,dato
        print ("######## TRADESAT SELL ############")
        nDati = 1
        try:
            response = self.caricaJSON(sellTradeApi)
            #print response
            #nDati = len(response["result"]["sell"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + sellTradeApi)
            print(response)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["result"]["sell"][a]["quantity"]))
                    dato.append(float(response["result"]["sell"][a]["rate"]))
                    dato.append("Tradesat Sell")
                    dato.append(sigla)
                return dato
            except (IndexError, TypeError) as error:
                print("#####################################")
                print("**ERROR1**")
                print response
                print("Something wrong, probably the market haven't " + sigla)
                print(error)
                print("#####################################")
                return []

