#ignore warnings
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import csv
import pandas as pd

def scrape(noRows, removeCategories = [], onlyCategories = [], csvName = 'pidgin_corpus.csv'):
    
    #noRows is the number of rows you need in your csv
    
    #removeCategories an optional variable or enter particular category you do not want or a list for more than 1 categories 
    
    
    
    csvfile = open(f"{csvName}",'w', newline='')
    obj = csv.writer(csvfile)
    headers=[('Media_name','Category', 'Headline', 'Brief_body', 'Report_Date', 'url', 'Body')]
    obj.writerows(headers)
    
    listNewsCategories = ['nigeria', 'africa', 'sport', 'entertainment']
    currentCount = 0
    
    try:
        if not removeCategories and onlyCategories:
        #only selected categories
            if isinstance(onlyCategories, list): 
                listNewsCategories = onlyCategories
            else:
                print(f'ERROR!: Parameter onlyCategories must be a list, and the available categories are {listNewsCategories}')
                return
        elif removeCategories and  not onlyCategories:
            #remove specific categories
            if isinstance(removeCategories, list): 
                listNewCategories = list(set(listNewsCategories).difference(set(removeCategories)))
            else:
                print(f'ERROR!: Parameter removeCategories must be a list, and the available categores are {listNewsCategories}')
                return 
    except Exception as e: print(e)
    
    allFromNews = True
    
    if noRows > len(listNewsCategories):
        noPerCategory = int(noRows / len(listNewsCategories))
        allFromNews = False
        
    
    if allFromNews == True:
        site = 'https://www.bbc.com/pidgin/topics/c404v061z85t'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site,headers=hdr)
        try:
            page = urlopen(req)
        except Exception as e: print(e)
        soup1 = BeautifulSoup(page)
        print('got here')
        
        for i in range(noRows):
            try:
                Headline = soup1.find_all("h3", {"class": "lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"})
                Headline = Headline[i].text
            except:
                Headline = "Nan"

            try:
                Brief_body = soup1.find_all("div", {"class": "gel-5/8@l"})
                Brief_body = Brief_body[i].text
                Brief_body = re.sub('Read Morenext', '', body)
            except:
                Brief_body = "Nan"

            try:
                Report_Date = soup1.find_all("span", {"class": "qa-post-auto-meta"})
                Report_Date = Report_Date[i].text
            except:
                Report_Date = "Nan"

            try:
                link = soup1.find_all("a", {"class": "qa-heading-link lx-stream-post__header-link"})
                link = link[i].get('href')
                link = f'https://www.bbc.com{link}'
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


                body = re.sub('\n', ' ', body)
                body = re.sub('Image copyright Others   Image example', ' ', body)
                body = re.sub('Image copyright', ' ', body)



            except:
                body = "Nan"
            
            entry = [('BBC Pidgin', 'nigeria', Headline, Brief_body, Report_Date, link, body)]
            obj.writerows(entry)
        
        
    else:
        
        for item in listNewsCategories:
            pageCount = 1
            rowCount = 0
            totalCount = 0

            for i in range(noPerCategory):

                if pageCount == 1:
                    if item == 'nigeria':
                        site= f"https://www.bbc.com/pidgin/topics/c2dwqd1zr92t"
                    elif item == 'africa':
                        site = 'https://www.bbc.com/pidgin/topics/c404v061z85t'
                    elif item == 'sport':
                        site = 'https://www.bbc.com/pidgin/topics/cjgn7gv77vrt'
                    elif item == 'entertainment':
                        site = 'https://www.bbc.com/pidgin/topics/cqywjyzk2vyt'


                    hdr = {'User-Agent': 'Mozilla/5.0'}
                    req = Request(site,headers=hdr)
                    try:
                        page = urlopen(req)
                        soup1 = BeautifulSoup(page)
                    except Exception as e: print(e)

                if rowCount == 10:
                    rowCount = 0 
                    pageCount +=1

                    if item == 'nigeria':
                        site= f"https://www.bbc.com/pidgin/topics/c2dwqd1zr92t/page/{pageCount}"
                    elif item == 'africa':
                        site = f'https://www.bbc.com/pidgin/topics/c404v061z85t/page/{pageCount}'
                    elif item == 'sport':
                        site = f'https://www.bbc.com/pidgin/topics/cjgn7gv77vrt/page/{pageCount}'
                    elif item == 'entertainment':
                        site = f'https://www.bbc.com/pidgin/topics/cqywjyzk2vyt/page/{pageCount}'

                    hdr = {'User-Agent': 'Mozilla/5.0'}
                    req = Request(site,headers=hdr)
                    try:
                        page = urlopen(req)
                        soup1 = BeautifulSoup(page)
                    except Exception as e: print(e)

               
                    
                #print(site)
                #print(noPerCategory)
                if item == "nigeria" and pageCount < 81 or item == "africa" and pageCount < 28 or item == "sport" and pageCount < 11 or item == "entertainment" and pageCount < 12:


                    category = item

                    try:
                        Headline = soup1.find_all("h3", {"class": "lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"})
                        Headline = Headline[rowCount].text
                    except:
                        Headline = "Nan"

                    try:
                        Brief_body = soup1.find_all("div", {"class": "gel-5/8@l"})
                        Brief_body = Brief_body[rowCount].text
                        Brief_body = re.sub('Read Morenext', '', body)
                    except:
                        Brief_body = "Nan"

                    try:
                        Report_Date = soup1.find_all("span", {"class": "qa-post-auto-meta"})
                        Report_Date = Report_Date[rowCount].text
                    except:
                        Report_Date = "Nan"

                    try:
                        link = soup1.find_all("a", {"class": "qa-heading-link lx-stream-post__header-link"})
                        link = link[rowCount].get('href')
                        link = f'https://www.bbc.com{link}'
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


                        body = re.sub('\n', ' ', body)
                        body = re.sub('Image copyright Others   Image example', ' ', body)
                        body = re.sub('Image copyright', ' ', body)



                    except:
                        body = "Nan"

                        
                    rowCount += 1
                    entry = [('BBC Pidgin', category , Headline, Brief_body, Report_Date, link, body)]
                    obj.writerows(entry)
                    
    csvfile.close()