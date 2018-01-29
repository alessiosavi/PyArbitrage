import json
import urllib2
from urllib2 import Request, URLError, urlopen
import time
import socket # socket.setdefaulttimeout(5.0) -> You can control the delay before socket.timeout is raised by calling socket.setdefaulttimeout(5.0).



hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}

socket.setdefaulttimeout(5.0)
def caricaJSON(self,url):
    request = None
    response = None
    try:
        request = Request(url, headers=Novaexchange.hdr)
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
