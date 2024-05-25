from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request

#if it says forbidden

def getLinks(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url,headers=hdr)
    response = urlopen(req)
    html_page=response.read()
    soup_page = soup(html_page,"lxml")
    links = []

    for link in soup_page.findAll('a'):
        links.append(link.get('href'))

    return links

url=input("Enter url: ")
print( getLinks(url) )
