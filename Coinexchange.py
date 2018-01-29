import json
import urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket # socket.setdefaulttimeout(5.0) -> You can control the delay before socket.timeout is raised by calling socket.setdefaulttimeout(5.0).

class Coinexchange:

    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}


    def initUrl(self,sigla):
        global urlCoinex
        sigla="281"
        urlCoinex = "https://www.coinexchange.io/api/v1/getorderbook?market_id="+ sigla
        return

    #Coinexchange have a strange methods for retrieve the coin. Instead the "ticker" (simple abbreviation), it use
    # a number ID for every market. In this function we need to map the coin name with the properly number
    def mapCoin(self,sigla):

        return



    socket.setdefaulttimeout(5.0)
    def caricaJSON(self,url):
        request = None
        response = None
        try:
            request = Request(url, headers=Coinexchange.hdr)
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


    def coinexListaSell(self,sigla):
        global urlCoinex,dato
        print ("######## COINEXCHANAGE SELL ############")
        nDati = 1
        try:
            response = self.caricaJSON(urlCoinex)
            #nDati = len(response["result"]["SellOrders"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + urlCoinex)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["result"]["SellOrders"][a]["Quantity"]))
                    dato.append(float(response["result"]["SellOrders"][a]["Price"]))
                    dato.append("CoinEx Sell")
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


    def coinexListaBuy(self,sigla):
        global urlCoinex, dato
        print ("######## COINEXCHANAGE BUY ############")
        nDati = 1
        try:
            response = self.caricaJSON(urlCoinex)
            #nDati = len(response["result"]["BuyOrders"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + urlCoinex)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["result"]["BuyOrders"][a]["Quantity"]))
                    dato.append(float(response["result"]["BuyOrders"][a]["Price"]))
                    dato.append("CoinEx Buy")
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