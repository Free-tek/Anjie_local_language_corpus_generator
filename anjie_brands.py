def anjie_brands(country, brand, csvName, startDate, endDate, numberOfRows):
    #TODO: show progress
    
    
    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen
    import re
    
    searchKeyword = brand

    

    if country == "all":
        #get news from punch
        site= f"https://punchng.com/search/{searchKeyword}"
        hdr = {'User-Agent': 'Mozilla/5.0'}
    
    
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)
        
        import csv
        csvfile = open(f"{csvName}.csv",'w', newline='')
        obj = csv.writer(csvfile)
        headers=[('Media_name','Brand_name', 'Headline', 'Brief_body', 'Report_Date', 'url')]
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
            
            
            entry = [('Punch NG', brand_name, Headline, Brief_body, Report_date, url)]
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
                
            entry = [('The Nation NG', brand_name, Headline, Brief_body, Report_date, url)]
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
   
            if Headline == "Nan":
                url == "Nan"
            else:
                #Get first paragraph as text summary
 
                #remove full stop inbetween figures in the link
                index = 0
                fullStopIndex = []
                for char in Headline:
                    if index != 0  and char is '.'and Headline[index-1].isdigit and Headline[index+1].isdigit:
                        fullStopIndex.append(Headline[index-1])
                        fullStopIndex.append(Headline[index+1])
                        Headline = Headline.replace(Headline[index],"-",1)
                    index = index + 1
            
                #replace hyphenes with whitespaces
                Headline_link  = Headline.replace('-', ' ')

                #remove punctuations

                pattern = r'[^\w\s]'
                pattern = pattern.replace("-", "")
                Headline_link = re.sub(pattern,'',Headline_link)
                #insert hyphens
                Headline_link = re.sub(r"\s+", '-', Headline_link)
                #change the headline to lowercase
                Headline_link = Headline_link.lower()
    
                if fullStopIndex != []:
                    index = Headline_link.find(fullStopIndex[0])
                    if Headline_link.find(fullStopIndex[1]) == index+1:
                        Headline_link = Headline_link[:index+1] + '-' + Headline_link[index+1:]
        
       
                #open the main page for this headline
                url = f'https://guardian.ng/news/{Headline_link}/'
    
    
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
    
    
            entry = [('The Guardian NG', brand_name, Headline_write, Brief_body, Report_date, url)]
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
    
            entry = [('BBC English', brand_name, Headline, Brief_body, Report_Date, url)]
            obj.writerows(entry)
        
        csvfile.close()
            
            
            
            
    
  
    
    
    
    
    
    
    

        