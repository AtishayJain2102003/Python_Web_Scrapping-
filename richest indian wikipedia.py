#richesh indians wikipedia
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

url="https://en.wikipedia.org/wiki/List_of_Indian_people_by_net_worth"

response=urlopen(url)
page_html=response.read()
page_soup=soup(page_html,"html.parser")

table=page_soup.find("table")
table_rows=table.findAll("tr")
richest_indians=[]
for table_row in table_rows:
    td=table_row.findAll("td")
    temp=[]
    for t in td:
        temp.append(t.text.strip("\n"))
    richest_indians.append(temp)

for richest_indian in richest_indians:
    print(richest_indian)

file=open("richest indian.csv","w")
csv_writer=csv.writer(file)
csv_writer.writerow(["Rank","Name","Net Worth","Field"])
for richest_indian in richest_indians:
    csv_writer.writerow(richest_indian)

file.close()




