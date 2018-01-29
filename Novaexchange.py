import json
import  urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket



# The main purpouse of this class is deserialize market from main Method.
class Novaexchange:

    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}

    def function(self):
        print(self.hdr)


    def initUrl(self,sigla):
        global urlNova,buyNovaApi,sellNovaApi
        urlNova  = "https://novaexchange.com/remote/v2/market/openorders/BTC_"+sigla
        buyNovaApi = urlNova + "/BUY/"
        sellNovaApi = urlNova + "/SELL/"
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


    def novaListaBuy(self,sigla):
        global buyNovaApi,dato
        print ("######## NOVA BUY ############")
        nDati = 1
        response=None
        try:
            response = self.caricaJSON(buyNovaApi)
            #nDati = len(response["buyorders"])
            #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + buyNovaApi)
            print(response)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["buyorders"][a]["amount"]))
                    dato.append(float(response["buyorders"][a]["price"]))
                    dato.append("Nova Buy")
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



    def novaListaSell(self,sigla):
        global sellNovaApi,dato
        print ("######## NOVA SELL ############")
        nDati = 1
        response=None
        try:
            response = self.caricaJSON(sellNovaApi)
        #        nDati = len(response["sellorders"])
        #print("Fetching " + str(nDati) + " orders")
        except TypeError as error:
            print("#####################################")
            print("TypeError, impossibile to fetch API: ")
            print("** API PROBABLY IN MAINTENANCE **")
            print(error)
            print("Curl -> " + sellNovaApi)
            print(response)
            print("#####################################")
            pass
        else:
            try:
                for a in range(nDati):
                    dato = []
                    dato.append(float(response["sellorders"][a]["amount"]))
                    dato.append(float(response["sellorders"][a]["price"]))
                    dato.append("Nova Sell")
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
                # \-> An empty list is needed for the correct execution of the future statment.
                #       This list will be ignored, because is empty, othere datatype can cause error at runtime.


