from selenium import webdriver
from bs4 import BeautifulSoup as bs 
import time
import csv
import requests
import pandas as pd 

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

web_Scraping_1 = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(web_Scraping_1)
print(page)

soup = bs(page.text,'html.parser')

table_of_stars =  soup.find('table')

temp_list = []
table_rows  = table_of_stars.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
Names_of_Stars = []
Distance_of_Stars = []
Mass_of_Stars = []
Radius_of_Stars = []

for i in range(1, len(temp_list)):
    Names_of_Stars.append(temp_list[i][1])
    Distance_of_Stars.append(temp_list[i][2])
    Mass_of_Stars.append(temp_list[i][3])
    Radius_of_Stars.append(temp_list[i][4])
    
    df2 = pd.DataFrame(list(zip(Names_of_Stars,Distance_of_Stars,Mass_of_Stars,Radius_of_Stars)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')    