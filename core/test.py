import requests
import urllib.parse
from bs4 import BeautifulSoup

dorks = "APISIX%2F2.12.1"
def single_scrap(dork, pages):
    urls = []
    proxie = {
        'http': "176.9.75.42:3128",
    }
    blacklist = ['support.google.com', 'accounts.google.com']
    try:
        for x in range(pages):
            pg = str(x*10)
            u = "https://www.google.com/search?q="+dork+"&start="+pg
            request = requests.get(u, proxies=proxie)
            resp = request.text
            soup = BeautifulSoup(resp, 'html.parser')
            links = soup.findAll('a')
            idnt = "&sa"
            for x in links:
                y = x['href']
                if y.startswith("/url?q="):
                    gg = y.replace("/url?q=", "")
                    hr = gg.split("&sa=")
                    hk = hr[0]
                    gf = hk.split("//")[1]
                    k = gf.split("/")[0]
                    if k in blacklist:
                        pass
                    else:
                        enc = urllib.parse.unquote(hk)
                        urls.append(enc)
        return urls
    except Exception:
        pass


print(single_scrap(dorks, 10))
