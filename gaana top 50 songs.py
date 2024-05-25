#gaana top 50 songs
from bs4 import BeautifulSoup as soup
from urllib.request import Request,urlopen
import csv

hdr={'User-Agent':"Mozilla/5.0"}
url="https://www.gaana.com/playlist/gaana-dj-bollywood-top-50-1"


req=Request(url,headers=hdr)
response=urlopen(req)
page_html=response.read()
page_soup=soup(page_html,"html.parser")

csv_file=open("Songs.csv","w",encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["Rank","Song Name"])

all_songs=page_soup.findAll("div",{"class":"playlist_thumb_det"})

for i in range(len(all_songs)):
    song_link=all_songs[i].find("a")
    song_name=song_link.text
    print(i+1,song_name)
    csv_writer.writerow([i+1,song_name])


csv_file.close()

