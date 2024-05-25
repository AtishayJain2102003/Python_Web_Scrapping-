from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

# Input from user

url = "https://www.youtube.com/results?search_query=latest+songs"

# Making the website believe that you are accessing it using a mozilla browser

req = Request(url, headers={'User-Agent': 'mozilla/5.0'})
page_html = urlopen(req).read()

page_soup = soup(page_html,'html.parser')

vids = page_soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)

print(videolist)
