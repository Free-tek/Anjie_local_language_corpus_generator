#ignore warnings
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
        
        
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as analyser
    
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
stopwords = stopwords.words('english')
    
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import csv
import pandas as pd
    
class englishCorpus():
  
    
    def _init_(self, noRows, removeCategories = [], onlyCategories = [], csvName = 'news'):
        
    def scrape(self):
    
    csvfile = open(f"{self.csvName}.csv",'w', newline='')
    obj = csv.writer(csvfile)
    headers=[('Media_name','Category', 'Headline', 'Brief_body', 'Report_Date', 'url', 'Body')]
    obj.writerows(headers)
    
    listNewsCategories = ['news', 'sports', 'metro-plus', 'politics', 'business', 'entertainment', 'editorial', 'columnist']
    currentCount = 0
    
    try:
        if not self.removeCategories and self.onlyCategories:
            #only selected categories
            if isinstance(self.onlyCategories, list): 
                listNewsCategories = self.onlyCategories
            else:
                print(f'ERROR!: Parameter onlyCategories must be a list, and the available categories are {listNewsCategories}')
                return
        elif self.removeCategories and  not self.onlyCategories:
            #remove specific categories
            if isinstance(self.removeCategories, list): 
                listNewCategories = list(set(listNewsCategories).difference(set(self.removeCategories)))
            else:
                print(f'ERROR!: Parameter removeCategories must be a list, and the available categores are {listNewsCategories}')
                return 
            
    except Exception as e: print(e)
                                
    allFromNews = True  
    try:
        if self.noRows > len(listNewsCategories):
            noPerCategory = int(self.noRows / len(listNewsCategories))
            allFromNews = False
    except Exception as e: print(e)
                                
            
            
    if allFromNews == True:
        site= f"https://punchng.com/topics/news/"
        hdr = {'User-Agent': 'Mozilla/5.0'}


        req = Request(site,headers=hdr)
        try:
            page = urlopen(req)
            soup = BeautifulSoup(page)
        except Exception as e: print(e)    
        
        category = "news" 
        
        for i in range(noRows):
            
    
            try:
                Headline = soup.find_all("div", {"class": "items col-sm-12"})
                Headline = Headline[i].a.get('title')
                #print(f"Headline: {Headline}")
            except:
                Headline = None
        
        
            try:
                briefBody = soup.find_all("div", {"class": "items col-sm-12"})
                briefBody = briefBody[i].find_all("div", {"class": "seg-summary"})
                briefBody = briefBody[0].find_all("p")
                briefBody = briefBody[0].text.strip()
                print(f"\nBriefBody: {briefBody}")
            except:
                briefBody = None
        
            try:
                date = soup.find_all("div", {"class": "items col-sm-12"})
                date = date[i].find_all("div", {"class": "seg-time"})
                date = date[0].find_all("span")
                date = date[0].text.strip()
                #print(f"\nDate: {date}")
            except:
                date = None
        
        
            try:
                link = soup.find_all("div", {"class": "items col-sm-12"})
                link = link[i].a.get('href')
                #print(f"\nLink: {link}")
            except:
                link = None
        
            try:
                req = Request(link,headers=hdr)
                page = urlopen(req)
                soup2 = BeautifulSoup(page)
        
                for script in soup2("script"):
                    script.extract()
        
                body = soup2.find_all("div", {"class": "entry-content"})
                body = body[0].get_text()
        
                sep = 'DOWNLOAD THE PUNCH NEWS APP NOW ON'
                body = body.split(sep, 1)[0]
                body = body.replace('(adsbygoogle = window.adsbygoogle || []).push({});','')
        
        
                #print(f"\nBody: {body}")
        
        
            except:
                body = None
        
            entry = [('Punch NG', 'News', Headline, briefBody, date, link, body)]
            obj.writerows(entry)
    else:
        
        for item in listNewsCategories:
            pageCount = 1
            rowCount = 0
            totalCount = 0
                
                
            site= f"https://punchng.com/topics/{item}/"
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = Request(site,headers=hdr)
            try:
                page = urlopen(req)
                soup = BeautifulSoup(page)
            except Exception as e: print(e)
                    
            for i in range(noPerCategory):
                
                if pageCount == 1:
                    site= f"https://punchng.com/topics/{item}/"
                    hdr = {'User-Agent': 'Mozilla/5.0'}
                    req = Request(site,headers=hdr)
                    try:
                        page = urlopen(req)
                        soup = BeautifulSoup(page)
                    except Exception as e: print(e)
                
                if rowCount == 12:
                    rowCount = 0 
                    pageCount +=1
                    
                    site= f'https://punchng.com/topics/{item}/page/{pageCount}/'
                    hdr = {'User-Agent': 'Mozilla/5.0'}
                    req = Request(site,headers=hdr)
                    try:
                        page = urlopen(req)
                        soup = BeautifulSoup(page)
                    except Exception as e: print(e)
                    
                rowCount += 1
                #print(site)
                if item == "news" and pageCount < 4550 or item == "sports" and pageCount < 1300 or item == "metro-plus" and pageCount < 980 or item == "politics" and pageCount < 650 or item == "business" and pageCount < 1250 or item == "entertainment" and pageCount < 250 or item == "editorial" and pageCount < 60 or item == "columnist" and pageCount < 340:
                    
                
                    category = item
                    
                
                    try:
                        Headline = soup.find_all("div", {"class": "items col-sm-12"})
                        Headline = Headline[rowCount].a.get('title')
                        #print(f"Headline: {Headline}")
                    except:
                        Headline = None
        
                    try:
                        briefBody = soup.find_all("div", {"class": "items col-sm-12"})
                        briefBody = briefBody[rowCount].find_all("div", {"class": "seg-summary"})
                        briefBody = briefBody[0].find_all("p")
                        briefBody = briefBody[0].text.strip()
                        #print(f"\nBriefBody: {briefBody}")
                    except:
                        briefBody = None
        
                    try:
                        date = soup.find_all("div", {"class": "items col-sm-12"})
                        date = date[rowCount].find_all("div", {"class": "seg-time"})
                        date = date[0].find_all("span")
                        date = date[0].text.strip()
                        #print(f"\nDate: {date}")
                    except:
                        date = None
        
        
                    try:
                        link = soup.find_all("div", {"class": "items col-sm-12"})
                        link = link[rowCount].a.get('href')
                        #print(f"\nLink: {link}")
                    except:
                        link = None
        
                    try:
                        req = Request(link,headers=hdr)
                        page = urlopen(req)
                        soup2 = BeautifulSoup(page)
        
                        for script in soup2("script"):
                            script.extract()
        
                        #body = soup.find_all("div", {"class": "row"})
                        body = soup2.find_all("div", {"class": "entry-content"})
                        body = body[0].get_text()
        
                        sep = 'DOWNLOAD THE PUNCH NEWS APP NOW ON'
                        body = body.split(sep, 1)[0]
                        body = body.replace('(adsbygoogle = window.adsbygoogle || []).push({});','')
        
        
                        #print(f"\nBody: {body}")
        
        
                    except:
                        body = None
                    
                entry = [('Punch NG', item, Headline, briefBody, date, link, body)]
                obj.writerows(entry)
            
            
            
    csvfile.close()