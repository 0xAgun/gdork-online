from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.parse
from bs4 import BeautifulSoup




urlss = []
address = []

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


def home(request):
    # return HttpResponse("homepage")
    return render(request, 'core/search.html')


def result(request):
    use_inp = request.GET.get('query')
    pages = request.GET.get('page')
    pages = int(pages)
    gear = single_scrap(use_inp, pages)
    hg = {'urls':gear}
    return render(request, 'core/rest.html', hg)