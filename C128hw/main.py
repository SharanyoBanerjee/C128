import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

bright_stars_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,"html.parser")

star_table = soup.find("table")

temp_list = []

table_row = star_table.find_all("tr")
for tr in table_row:
    td = tr.find_all('td')

row = [i.text.rstrip() for i in td ]
temp_list.append(row)

star_name = []
distance = []
mass = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
    
df2 = pd.DataFrame(list(zip(star_name,distance,radius,mass)),columns = ['star_name','distance','mass','radius'])
print(df2)

df2.to_csv("bright_star.csv")
