#ignore warnings
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
        
        

    
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import csv
import pandas as pd


def scrape_hausa(no_rows, csvName = 'hausa_news.csv'):
    csvfile = open(f'{csvName}','w', newline='')
    obj = csv.writer(csvfile)
    headers=[('BBC Hausa', 'Headline', 'Brief_body', 'Report_Date', 'Url_link', 'body')]
    obj.writerows(headers)

    if no_rows > 60:
        print('Only 60 rows available for news in hausa language')
    else:
        noPerCategory = no_rows//3
    
    for i in range(3)
        if i == 0:
            #sports
            site = 'https://www.bbc.com/hausa/wasanni'
        elif i == 1:
            #review
            site = 'https://www.bbc.com/hausa/mujalla'
        elif 1 == 2:
            #full reports
            site = 'https://www.bbc.com/hausa/rahotanni'
            
        req = Request(site,headers=hdr)
        try:
            page = urlopen(req)
        except Exception as e: print(e)
            soup1 = BeautifulSoup(page)


        for i in range(noPerCategory):
            try:
                Headline = soup1.find_all("h3", {"class": "title-link__title"})
                Headline = Headline[i].text
            except:
                Headline = "Nan"
    
            try:
                Brief_body = soup1.find_all("p", {"class": "eagle-item__summary"})
                Brief_body = Brief_body[i].text
            except:
                Brief_body = "Nan"
    
            try:
                Report_Date = soup1.find_all("ul", {"class": "mini-info-list"})
                Report_Date = Report_Date[i].text
            except:
                Report_Date = "Nan"
    
            try:
                link = soup1.find_all("div", {"class": "eagle-item__body"})
                link = link[i].find_all("a", {"class": "title-link"})
                link = link[0].get("href")
                link = f'https://www.bbc.com/{link}'
            except:
                link = "Nan"

            
            try:
                req = Request(link,headers=hdr)
                try:
                    page = urlopen(req)
                    soup2 = BeautifulSoup(page)

                    for script in soup2("script"):
                        script.extract()
                except Exception as e: print(e)

                body = soup2.find_all("div", {"class": "story-body__inner"})
                body = body[0].text.strip()

                body = body.replace('Image caption','')
                body = body.replace('Getty Images','')


            except:
                body = "Nan"
            
            entry = [('BBC Hausa', Headline, Brief_body, Report_Date, link, body)]
            obj.writerows(entry)
        
   
            
