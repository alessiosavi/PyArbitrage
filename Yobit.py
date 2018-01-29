import json
import urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket # socket.setdefaulttimeout(5.0) -> You can control the delay before socket.timeout is raised by calling socket.setdefaulttimeout(5.0).

class Yobit:

    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}

    def initUrl(self,sigla):
        #								/->price	/-> amount			/->price	/-> amount
        # --- YOBIT --- ***{"asks":[[ 0.00000341 , 474.87636943],  .... ], "bids":[[ 0.00000323 , 5615.13043478 ] ...]} ***
        global urlYobit
        urlYobit = "https://yobit.net/api/2/"+sigla+"_btc/depth"
        return

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




    def yobitListaBuy(self,sigla):
        global urlYobit
        print ("######## YoBIT BUY ############")
        nDati = 1
        try:
            response = self.caricaJSON(urlYobit)
            #nDati = len(response["asks"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + urlYobit)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["bids"][a][1]))  # amount
                    dato.append(float(response["bids"][a][0]))  # price, rate
                    dato.append("YoBit Buy")
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



    def yobitListaSell(self,sigla):
        global urlYobit
        print ("######## YoBIT SELL ############")
        nDati = 1
        try:
            response = self.caricaJSON(urlYobit)
            #nDati = len(response["bids"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + urlYobit)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["asks"][a][1]))  # amount
                    dato.append(float(response["asks"][a][0]))  # price, rate
                    dato.append("YoBit Sell")
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
