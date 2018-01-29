import json
import urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket # socket.setdefaulttimeout(5.0) -> You can control the delay before socket.timeout is raised by calling socket.setdefaulttimeout(5.0).

class Ccex:


    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}


    def initUrl(self,sigla):
        global urlCcex,buyCexApi,sellCexApi
        urlCcex = "https://c-cex.com/t/api_pub.html?a=getorderbook&market="
        buyCexApi = urlCcex+sigla+"-btc&type=buy&depth=3"
        sellCexApi = urlCcex+sigla+"-btc&type=sell&depth=3"
        return

    socket.setdefaulttimeout(5.0)
    def caricaJSON(self,url):
        request = None
        response = None
        try:
            request = Request(url, headers=Ccex.hdr)
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



    def cexListaBuy(self,sigla):
        global buyCexApi,dato
        print ("######## C-CEX BUY ############")
        response = None
        nDati = 1
        try:
            response = self.caricaJSON(buyCexApi)
            #nDati = len(response["result"]["buy"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(str(error))
            print("Curl -> " + urlopen(Request(buyCexApi, headers=self.hdr)).read())
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["result"]["buy"][a]["Quantity"]))
                    dato.append(float(response["result"]["buy"][a]["Rate"]))
                    dato.append("CCEX Buy")
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


    def cexListaSell(self,sigla):
        global sellCexApi,dato
        print ("######## C-CEX SELL ############")
        response = None
        nDati = 1
        try:
            response = self.caricaJSON(sellCexApi)
            #nDati = len(response["result"]["sell"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as typeError:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(str(typeError))
            print("Curl -> " + urlopen(Request(sellCexApi, headers=self.hdr)).read())
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["result"]["sell"][a]["Quantity"]))
                    dato.append(float(response["result"]["sell"][a]["Rate"]))
                    dato.append("CCEX Sell")
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

