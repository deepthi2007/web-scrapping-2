from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,'html.parser')
starTable = soup.find_all('table')
temp_list =[]

tableRow = starTable[7].find_all('tr')

for tr in tableRow :
    td=tr.find_all('td')
    rows = [i.text.rstrip() for i in td]
    temp_list.append(rows)

Star_names =[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Star_names,distance,mass,radius)))
print(df2)
df2.to_csv("dwarf_stars.csv")