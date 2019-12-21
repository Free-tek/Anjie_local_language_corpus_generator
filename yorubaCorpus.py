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
 
def scrape(noRows, csvName = 'yoruba_corpus.csv'):
    
    
    csvfile = open(f'{csvName}','w', newline='')
    obj = csv.writer(csvfile)
    headers=[('BBC Yoruba', 'Headline', 'Brief_body', 'Report_Date', 'Url_link', 'body')]
    obj.writerows(headers)

    site = "https://www.bbc.com/yoruba"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    try:
        page = urlopen(req)
    except Exception as e: print(e)
    soup = BeautifulSoup(page)
    
    major = soup.find_all("h3", {"class": "Headline-sc-1dvfmi3-4 cWuUJx"})

    count  = 0
    for i in range(len(major)):
        count+=1
        try:
            if i == 0:
                Headline = soup.find_all("h3", {"class": "Headline-sc-1dvfmi3-4 kZxQqx"})
                Headline = Headline[0].text
            else:
                Headline = soup.find_all("h3", {"class": "Headline-sc-1dvfmi3-4 cWuUJx"})
                Headline = Headline[i].text
        except:
            Headline = "Nan"

       
        try:
            if i == 0 :
                Report_Date = soup.find_all("div", {"class": "TextGridItem-sc-1dvfmi3-6 cLkEbv"})
                Report_Date = Report_Date[0].find_all("time", {"class": "StyledTimestamp-um718p-0 kVWTyt"})
                Report_Date = Report_Date[0].text
            else:
                Report_Date = soup.find_all("div", {"class": "TextGridItem-sc-1dvfmi3-6 fdmIIY"})
                Report_Date = Report_Date[i].find_all("time", {"class": "StyledTimestamp-um718p-0 kVWTyt"})
                Report_Date = Report_Date[0].text
        except:
            Report_Date = "Nan"
        
        try:
            if i == 0:
                url = soup.find_all("h3", {"class": "Headline-sc-1dvfmi3-4 kZxQqx"})
                url = url[0].a.get("href")
                url = f"https://www.bbc.com{url}"

                req = Request(url,headers=hdr)
                page = urlopen(req)
                soup2 = BeautifulSoup(page)
            
                Brief_body = soup2.find_all("p", {"class": "story-body__introduction"})
                Brief_body = Brief_body[0].text
            else:
                Brief_body = soup.find_all("p", {"class": "Summary-sc-1dvfmi3-5 itgvLR"})
                Brief_body = Brief_body[i].text
        except:
            Brief_body = "Nan"
                
            
        try:
            if i == 0:
                link = url
            else:
                link = soup.find_all("h3", {"class": "Headline-sc-1dvfmi3-4 cWuUJx"})
                link = link[i].a.get("href")
                link = f"https://www.bbc.com{link}"
        except:
            link = "Nan"
        
        try:
            if link != "Nan":
                req = Request(link,headers=hdr)
                try:
                    page = urlopen(req)
                    soup2 = BeautifulSoup(page)
                except Exception as e: print(e)
            
        
            body = soup2.find_all("div", {"class": "story-body__inner"})
            body = body[0].text
            
        except:
            body = "Nan"
        
    
        
    
        entry = [('BBC Yoruba', Headline, Brief_body, Report_Date, link, body)]
        obj.writerows(entry)
    
    
    while count < noRows:
        j = 0
        for j in range(6):


            if j == 0:
                site2 = "https://www.bbc.com/yoruba/topics/c340q0y3p5kt"
                j+=1
            else:
                site2 = f"https://www.bbc.com/yoruba/topics/c340q0y3p5kt/page/{j}"
                req = Request(site2,headers=hdr)
            try:
                page = urlopen(req)
            except Exception as e: 
                print(e)
            
            soup1 = BeautifulSoup(page)
        
        

            major2 = soup1.find_all("h3", {"class": "lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"})

            for i in range(len(major2)):
                count+=1
                try:
                    if i == 0:
                        Headline = soup1.find_all("h3", {"class": "lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"})
                        Headline = Headline[0].text
                    else:
                        Headline = soup1.find_all("h3", {"class": "lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-"})
                        Headline = Headline[i].text
                except:
                    Headline = "Nan"

    
       
                try:
                    if i == 0 :
                        Report_Date = soup1.find_all("span", {"class": "qa-post-auto-meta"})
                        Report_Date = Report_Date[0].text
                    else:
                        Report_Date = soup1.find_all("span", {"class": "qa-post-auto-meta"})
                        Report_Date = Report_Date[i].text
                except:
                    Report_Date = "Nan"

    
        
                try:
                    Brief_body = soup1.find_all("p", {"class": "lx-stream-related-story--summary qa-story-summary"})
                    Brief_body = Brief_body[i].text.strip()
                except:
                    Brief_body = "Nan"
            
    
    
    
                try:
                    link = soup1.find_all("a", {"class": "qa-heading-link lx-stream-post__header-link"})
                    link = link[i].get("href")
                    link = f'https://www.bbc.com/{link}'
                except:
                    link = "Nan"
    
                try:
                    req = Request(link,headers=hdr)
                    try:
                        page = urlopen(req)
                        soup2 = BeautifulSoup(page)
                    except Exception as e: print(e)
                    
                    body = soup2.find_all("div", {"class": "story-body__inner"})
                    body = body[0].text.strip()
                except:
                    body = "Nan"
            
        entry = [('BBC Yoruba', Headline, Brief_body, Report_Date, link, body)]
        obj.writerows(entry)
        
       
        
    if count >= noRows:
        csvfile.close()
        
    


