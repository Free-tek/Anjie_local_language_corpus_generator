def anjie_brands(country, brand, csvName):
    #TODO: show progress
    
    
    
    #ignore warnings
    import warnings
    warnings.filterwarnings("ignore")
    
    import matplotlib.pyplot as plt; 
    import numpy as np
    import matplotlib.pyplot as plt
        
        
    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer as analyser

    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen
    import re
    import csv
    import pandas as pd
    
    searchKeyword = brand

    

    if country == "all":
        #get news from punch
        site= f"https://punchng.com/search/{searchKeyword}"
        hdr = {'User-Agent': 'Mozilla/5.0'}


        req = Request(site,headers=hdr)
        try:
            page = urlopen(req)
        except Exception as e: print(e)
        
        soup = BeautifulSoup(page)
        
        
        csvfile = open(f"{csvName}.csv",'w', newline='')
        obj = csv.writer(csvfile)
        headers=[('Media_name','Brand_name', 'Headline', 'Brief_body', 'Report_Date', 'url', 'polarity_score')]
        obj.writerows(headers)
    
    
        major = soup.find_all("h2", {"class": "seg-title"})        
        for i in range (len(major)):
            brand_name = searchKeyword
            try:
                Headline = soup.find_all("h2", {"class": "seg-title"})
                Headline = Headline[i].text
            except:
                Headline = "Nan"
                
            try:
                Brief_body = soup.find_all("div", {"class": "seg-summary"})
                Brief_body = Brief_body[i].text.strip()
            except:
                Brief_body = "Nan"
                
            try:
                Report_date = soup.find_all("div", {"class": "seg-time"})            
                Report_date = Report_date[i].text.strip()
            except:
                Report_date = "Nan"
              
            try:
                #TODO: 900 pages scenario
                
                #remove punctuations
                Headline_link = re.sub(r'[^\w\s]','',Headline)
               
                #insert hyphens
                Headline_link = re.sub(r"\s+", '-', Headline_link)

                #change the headline to lowercase
                Headline_link = Headline_link.lower()

                #open the main page for this headline
                url = f'https://punchng.com/{Headline_link}/'
            except:
                url = "Nan"
            
            #get sentiment analysis
            sia = analyser()
            results = []
            polarity_score = sia.polarity_scores(Headline)
            
            entry = [('Punch NG', brand_name, Headline, Brief_body, Report_date, url, polarity_score)]
            obj.writerows(entry)
            
          
        #get news from the nation
        site = f'https://thenationonlineng.net/?s={searchKeyword}'
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)
        
        
        
        major = soup.find_all("h3", {"class": "jeg_post_title"})

        for i in range (len(major)):
            brand_name = searchKeyword
            try:
                Headline = soup.find_all("h3", {"class": "jeg_post_title"})
                Headline = Headline[i].text.strip()
                if searchKeyword not in Headline:
                    break
        
            except:
                Headline = "Nan"
        
            try:
                Brief_body = soup.find_all("div", {"class": "jeg_post_excerpt"})
                Brief_body = Brief_body[i].text.strip()
            except:
                Brief_body = "Nan"
            
            try:
                Report_date = soup.find_all("div", {"class": "jeg_meta_date"})            
                Report_date = Report_date[i].text.strip()
            
            except:
                Report_date = "Nan"
                
            try:
                #remove punctuations
                Headline_link = re.sub(r'[^\w\s]','',Headline)
                #insert hyphens
                Headline_link = re.sub(r"\s+", '-', Headline_link)
                #change the headline to lowercase
                Headline_link = Headline_link.lower()
                #open the main page for this headline
                url = f'https://thenationonlineng.net/{Headline_link}/'
        
            except:
                url = "Nan"
           
            #get sentiment analysis
            sia = analyser()
            results = []
            polarity_score = sia.polarity_scores(Headline)
                
            entry = [('The Nation NG', brand_name, Headline, Brief_body, Report_date, url, polarity_score)]
            obj.writerows(entry)

            
        # get news from gurdian
        site = f'https://guardian.ng/?s={searchKeyword}'
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)
        
        
        major = soup.find_all("div", {"class": "headline"})
        for i in range(len(major)):
    
            #Get headline
            try:
                Headline = soup.find_all("div", {"class": "headline"})
                Headline = Headline[i].find_all("span", {"class": "title"})[0].text
                Headline = BeautifulSoup(Headline, "lxml").text
                Headline_write = Headline
                if searchKeyword not in Headline:
                    break
            except:
                Headline = "Nan"
                Headline_write = "Nan"
   
            try:
                url = soup.find_all("a", {"data-field": "link"})
                url = url[i].get("href")
            except:
                url = "Nan"
           
            #open the main page for this headline
            if url == "Nan":
                Brief_body = "Nan"
            else:
                req = Request(url,headers=hdr)
                page = urlopen(req)
                soup_2 = BeautifulSoup(page)
                Brief_body = soup_2.find_all("article")
                Brief_body = Brief_body[0].find_all("p")[2].text
    
    
            #Get report Date
            try:
                Report_date = soup.find_all("div", {"class": "meta"})
                Report_date = Report_date[i].find_all("span", {"class": "age"})[0].text
            except: Report_date = "Nan"
            
            #get sentiment analysis
            sia = analyser()
            results = []
            polarity_score = sia.polarity_scores(Headline_write)
    
            entry = [('The Guardian NG', brand_name, Headline_write, Brief_body, Report_date, url, polarity_score)]
            obj.writerows(entry)
            
            
            
            
            
        #Scarpe BBC
        site = f'https://www.bbc.co.uk/search?q={searchKeyword}'
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)
        
        
        major = soup.find_all("h1", {"itemprop": "headline"})
        for i in range(len(major)):
    
            #Get headline
            try:
                Headline = soup.find_all("h1", {"itemprop": "headline"})
                Headline = Headline[i].text
            except:
                Headline = "Nan"
    
            #Get Date
            try:
                Report_Date = soup.find_all("li", {"data-result-number": i+1})
                Report_Date = Report_Date[0].find_all("time", {"class": "display-date"})
                Report_Date = Report_Date[0].text.strip()
            except:
                Report_Date = "Nan"

    
            #Brief Body
            #BBC has summary long, medium and short this can be made available to the user
            try:
                Brief_body = soup.find_all("li", {"data-result-number": i+1})
                Brief_body = Brief_body[0].find_all("p", {"class": "summary long"})
                Brief_body = Brief_body[0].text.strip()
            except:
                Brief_body = "Nan"
        
            ##get post link
            try:
                link = soup.find_all("h1", {"itemprop": "headline"})
                link = link[i].a.get("href")
            except:
                link = "Nan"
            
            #get sentiment analysis
            sia = analyser()
            results = []
            polarity_score = sia.polarity_scores(Headline)
    
            entry = [('BBC English', brand_name, Headline, Brief_body, Report_Date, url, polarity_score)]
            obj.writerows(entry)
            
            
        #scrape from lindaikeji's blog
        brand_name = "MTN"
        site = f"https://www.lindaikejisblog.com/search/result?search={brand_name}"
        
        req = Request(site,headers=hdr)
        try:
            page = urlopen(req)
        except Exception as e: print(e)
        soup = BeautifulSoup(page)

        major = soup.find_all("article", {"class": "result"})

        for i in range(len(major)):
            try:
                Headline = soup.find_all("a", {"class": "title"})
                Headline = Headline[i].text
                Headline
            except:
                Headline = "Nan"
        
        
      
            try:
                pattern = re.compile(r'\n\xa0\n')

                Brief_body = soup.find_all("summary", {"class": "description"})
                Brief_body = Brief_body[i].text.strip()
                Brief_body = pattern.sub('', Brief_body)
            except:
                Brief_body = "Nan"
    
        
        
            try:
                patternDate = re.compile(r'by Linda Ikeji at ')

                Report_Date = soup.find_all("div", {"class": "post_age"})
                Report_Date = Report_Date[i].text.strip()
                Report_Date = patternDate.sub('', Report_Date )
            except:
                Report_Date = "Nan"
    
            try:
                url = soup.find_all("a", {"class": "title"})
                url = url[i].get("href")
            except:
                url = "Nan"
            
            #get sentiment analysis
            sia = analyser()
            results = []
            polarity_score = sia.polarity_scores(Headline)
            
            entry = [('Lindaikeji\'s blog', brand_name, Headline, Brief_body, Report_Date, url, polarity_score)]
            obj.writerows(entry)
            
            
            
        #scrape from news24 southAfrica
        site = f"https://www.news24.com/Tags/Topics/{brand_name}"
        req = Request(site,headers=hdr)
        try:
            page = urlopen(req)
        except Exception as e: print(e)
        soup = BeautifulSoup(page)

        major = soup.find_all("div", {"class": "col300 news_item"})

        for i in range(len(major)):
            try:
                Headline = soup.find_all("h4")
                pattern = re.compile(r'â\x80\x93')
                Headline = Headline[i].text.strip()
                Headline = pattern.sub('', Headline)
            except:
                Headline = "Nan"
     
            try:
                major2 = soup.find_all("div", {"class": "left vert_line col314"})
                Brief_body = major2[0].find_all("p")
                Brief_body = Brief_body[i].text.strip()
            except:
                Brief_body = "Nan"
            if Brief_body == "Nan":
                try:
                    major2 = soup.find_all("div", {"class": "col300 news_item"})
                    Brief_body = major2[i].find_all("p")
                    Brief_body = Brief_body[0].text.strip()
                except:
                    Brief_body = "Nan"
            try:
                Report_Date = soup.find_all("span", {"class": "block datestamp left"})
                Report_Date = Report_Date[i].text.strip()
            except:
                Report_Date = "Nan"
            try:
                url = soup.find_all("div", {"class": "col300 news_item"})
                url = url[i].find_all("a")
                url = url[0].get("href")
            except:
                url = "Nan"
                
            #get sentiment analysis
            sia = analyser()
            results = []
            polarity_score = sia.polarity_scores(Headline)
            
            entry = [('News24', brand_name, Headline, Brief_body, Report_Date, url, polarity_score)]
            obj.writerows(entry)
            
            
        csvfile.close()
        
        df = pd.read_csv(f"{csvName}.csv")
        
        polar = []
        result = []
        
        df['polarity_score1'] = ""
        
        vader = analyser()
        for i in range (len(df)):
            polar.append(vader.polarity_scores(df['Headline'][i])['compound'])
            if polar[i] >= 0.2:
                result.append("Positive")
                df['polarity_score1'][i] == "Positive"
            else:
                result.append("Negative")
                df['polarity_score1'][i] == "Negative"
     
            
        
        y_pos = ['Positive', 'Negative']
        
        print("These are the newspapers and how their posts pass, positive or negative")
        print(df.groupby(['Media_name', 'polarity_score1'])['polarity_score1'].count())
        
        array = [(result.count('Positive')/len(df)) * 100, (result.count('Negative')/ len(df)) * 100]
        plt.bar(y_pos, array, align='center', alpha=0.5)
        plt.xticks(y_pos)
        plt.ylabel('Counts')
        plt.title('Brand analysis for ')
        plt.show()
        
        
            

            
    
  
    
    
    
    
    
    
    

        
