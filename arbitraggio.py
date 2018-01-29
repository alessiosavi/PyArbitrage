#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket # socket.setdefaulttimeout(5.0) -> You can control the delay before socket.timeout is raised by calling socket.setdefaulttimeout(5.0).
from Novaexchange import  Novaexchange
from Ccex import  Ccex
from Tradesatoshi import  Tradesatoshi
from Yobit import Yobit
from Coinexchange import  Coinexchange

# numero coin -> 2->3coin (0 1 2)
COUNTER=None
coinexBuy=None
coinexSell=None


novaexchange=Novaexchange()
ccex=Ccex()
tradesatoshi=Tradesatoshi()
coinexchange=Coinexchange()
yobit=Yobit()

hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}

# Input: API url
# Output: JSON Object

#If you wanna change a content of a variable then you need to use a "global" keyword in a function.
def initUrl(sigla):
    global  urlCoinex
    novaexchange.initUrl(sigla)
    ccex.initUrl(sigla)
    tradesatoshi.initUrl(sigla)
    yobit.initUrl(sigla)
    urlCoinex = "https://www.coinexchange.io/api/v1/getorderbook?market_id=281"
    return


def checkLista(lista):
    #print "############### CHECK-LISTA #####################"
    for item in lista:
        if not item:
            print item
            lista.remove(item)
    return lista


def printer():
    print(novaSell)
    print(novaBuy)
    print(cexSell)
    print(cexBuy)
    print(yobitSell)
    print(yobitBuy)
    return

def init(sigla):
    global novaSell, novaBuy, cexSell ,cexBuy ,tradeSell ,tradeBuy ,yobitSell ,yobitBuy ,coinexSell ,coinexBuy
    deleteAll()
    novaSell=novaexchange.novaListaSell(sigla)
    novaBuy=novaexchange.novaListaBuy(sigla)
    cexSell=ccex.cexListaSell(sigla)
    cexBuy=ccex.cexListaBuy(sigla)
    tradeSell=tradesatoshi.tradeListaSell(sigla)
    tradeBuy=tradesatoshi.tradeListaBuy(sigla)
    yobitSell=yobit.yobitListaSell(sigla)
    yobitBuy=yobit.yobitListaBuy(sigla)
    #coinexSell=coinexListaSell(sigla)
    #coinexBuy=coinexListaBuy(sigla)

def deleteAll():
    global novaSell, novaBuy, cexSell, cexBuy, tradeSell, tradeBuy, yobitSell, yobitBuy, coinexSell, coinexBuy
    novaSell = []
    novaBuy = []
    cexSell = []
    cexBuy = []
    tradeSell = []
    tradeBuy = []
    yobitSell = []
    yobitBuy = []

def printJson(nomeFile,lista):
    with open(nomeFile,'w') as outFile:
        json.dump(lista,outFile)
    return


def findOpportunities():
    global VENDO_A, COMPRO_A, novaSell, cexSell, yobitSell, tradeSell , novaBuy, cexBuy, yobitBuy, tradeBuy, coinexBuy,coinexSell
    VENDO_A=COMPRO_A=0
    tempsell = [novaSell, cexSell, yobitSell, tradeSell, coinexSell]
    tempbuy = [novaBuy, cexBuy, yobitBuy, tradeBuy , coinexBuy]
    #sell = [novaSell, cexSell, yobitSell,tradeSell]  # tradeSell[0], coinexSell[0]]
    #buy = [novaBuy, cexBuy, yobitBuy,tradeBuy]  # , tradeBuy[0], coinexBuy[0]
    #sell=checkLista(sell)
    #buy=checkLista(buy)
    sell=filter(None,tempsell)
    buy=filter(None,tempbuy)
    print("Lista Buy: "+str(sell))
    print("Lista Sell: "+str(buy))
    ## NEED A TRY CATCH
    VENDO_A = max(buy, key=lambda x: x[1])
    COMPRO_A = min(sell, key=lambda x: x[1])

    print(str(VENDO_A))
    print(str(COMPRO_A))
    if (float(VENDO_A[1]) > float(COMPRO_A[1])):
        #print("                                     **** YAY! ****")
        #print ("Compro a:" + str(COMPRO_A))
        #print ("Vendo a:" + str(VENDO_A))
        return 1
    else:
        print("Next time (: ")
        print("No profitable trading moves found :(")
        return 0



# This method take as input the number of max coin tradable, and check the profit
# [amount, price]
def checkProfit(coinName):
    global COUNTER
    COUNTER=0
    BTC_PRICE=13000
    flag=findOpportunities()
    coinPriceBuy=COMPRO_A
    coinPriceSell=VENDO_A
    amount=coinAmount(coinPriceBuy,coinPriceSell)#min amount of coin to trade
    minMoney=amount*COMPRO_A[1]*BTC_PRICE # min money to move for gain, COMPRO_A is every time lowest than VENDO, in other case, we are in losses (:
    if (flag==1):
        print("               /->SELL<-\\                                 /->BUY<-\\ ")
        print(str(coinPriceSell)+ "/"+str(coinPriceBuy)+"--> "+ str(amount) +" COIN  [SPREAD "+str((coinPriceSell[1]- coinPriceBuy[1])*BTC_PRICE)+" €], Need "+ str(minMoney) + " €")
        compro=amount*coinPriceBuy[1]
        vendo=amount*coinPriceSell[1]
        gain=vendo-compro
        print("Guadagno potenziale-> "+str(gain) +" BTC"+" ["+ str(gain*BTC_PRICE)+" €]")
        print("")
        print ("")
        #printJson("buy" + str(COUNTER) + ".json", COMPRO_A)
        #printJson("sell" + str(COUNTER) + ".json", VENDO_A)
        #printJson("gain"+str(COUNTER)+".json", str(gain))
        COUNTER += 1
        return
    else:
        print("Next time man ;)")



# find the max coin that you can trade
 # [amoount, price]
def coinAmount(a,b):
    lista=[a,b]
    amount= min(lista, key=lambda x: x[0])
    return amount[0]



# This method need to iterate different market and fetch the price.
def iterateMarket():
    global VENDO_A,COMPRO_A,listaSell,listaBuy
    listaCoin=["dash","etc","ltc","doge"]#,"bch","BTG","BCC","DOGE","CNT","DCR","DGB"]
    for i in listaCoin:
        #sigla=(listaCoin[i])
        print ("                                     ** ## Sigla Moneta ## **")
        print("                                             \->"+ i +"<-/")
        print(str(i))
        initUrl(str(i))
        init(str(i))
        checkProfit(i)



iterateMarket()

for i in range(15):
    iterateMarket()
    print("#############################################")
    time.sleep(2)





