from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 
brightstare_URL ="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(brightstare_URL)
soup=bs(page.text,'html.parser')
star=soup.find('table')
erf=[]
table_row=star.find_all('tr')
for tr in table_row:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    erf.append(row)
print(erf)
starname=[]
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")
