import re
import requests
import geoip2.database

def transfer(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip='
    resp = requests.get(url + ip)
    return resp


def Iplocation(ip):
    response = geoip2.database.Reader("./GeoLite2-City.mmdb").city(ip)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Hosts': 'www.gpsspg.com',
        'Referer': 'http://www.gpsspg.com/iframe/maps/qq_161128.htm?mapi=2',
    }
    url = "http://www.gpsspg.com/apis/maps/geo/?output=jsonp&lat=%s000000&lng=%s000000&type=0&callback=jQuery110207785323396673127_1522316918197&_=1522316918198" % (
    response.location.latitude, response.location.longitude)
    try:
        return re.findall("address\"\:\"(.+?)\"", requests.get(url, headers=headers).text)[0]
    except Exception as e:
        return e


if __name__ == '__main__':
    # transfer('116.236.221.186')
    print(Iplocation('116.236.221.186'))
    import random
    random._urandom(132)