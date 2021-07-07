This python library provides corpus in English and various local african languages e.g(Youruba, Hausa, Pidgin) by scraping several online newspaper websites, it also does sentiment analysis on brands and can tell you if your brand is looking good or bad from various media publications.

<b>USAGE</b>

<b>Brand Sentiment Analysis</b>

This method helps you scrape news from 7 online english written newspapers and blogs for a particular organisation or brand and can run sentiment analysis to 
tell you how the brand is percieved in the news.

<p>
  The list of online newspapers this script scrapes from is
  <br> Punch
  <br> The Nation Newspaper
  <br> The Guardian Newspaper
  <br> BBC
  <br> Lindaikeji's blog
  <br> News24
  
<p>
Most recent developments to this library will allow you scrape news from various news papers and blogs across the world and we hope that you use
the corpus you generate to do some awesome machine learning tasks.
  
<br>
<b>Brand analaysis on Donald Trump</b>
<br>
<br>
<image src = "https://github.com/Free-tek/Worldwide-Newspaper-Scraping-Script/blob/master/Screenshot%202019-11-15%20at%206.27.52%20pm.png">

https://pypi.org/project/anjie-adewole63/0.0.1/

<br>
<b>HELP</b>

```
brand = "MTN" #the name of the brand you will like to perfrom sentiment analysis on e.gcsvFileName = The name of the csv file you will like to save your output to, default is brandNews.csv. (optional parameter)
from anjie import brandSentimentAnalysis
brandSentimentAnalysis.anjie_brands(brand = "MTN", csvFileName = 'brandNews')
```
  
```
import pandas as pd
df = pd.read_csv("brandNews.csv.csv")
```


<b>Scraping English Corpus</b>

noRows = 2 The number of rows of news you want.
<br>csvFileName = "my_result.csv" The name of the csv file you will like to save your output to, default is news.csv. (optional parameter)
<br>News categories include ['news', 'sports', 'metro-plus', 'politics', 'business', 'entertainment', 'editorial', 'columnist']
<br>removeCategories = [] :as a parameter for news categories you don't want in the scraped corpus. (optional parameter)
e.g.
  
```
englishCorpus.scrape(noRows = 150, removeCategories = ['metro-plus', 'politics']) 
```
  
pass onlyCategories = [] : as a parameter for only categories you want in the scraped corpus. (optional parameter)
e.g , 
```
englishCorpus.scrape(noRows = 150, onlyCategories = ['news', 'sports', 'metro-plus', 'entertainment', 'editorial', 'columnist'])
```
  
```
from anjie import englishCorpus
englishCorpus.scrape(noRows = 150)
df = pd.read_csv("news.csv")
```
  
  
<b>Scraping Hausa Corpus</b>
<br>
noRows = 2 The number of rows of news you want. only 60 rows of hausa corpus is currently available.
<br>
csvName = "my_result.csv" The name of the csv file you will like to save your output to, default is hausa_news.csv. (optional parameter) 

```
from anjie import hausaCorpus
hausaCorpus.scrape(noRows = 10)
import pandas as pd
df = pd.read_csv("hausa_news.csv")
```
  
<b>Scraping Pidgin English corpus</b>
<br>
noRows = 2 The number of rows of news you want.
<br>
csvFileName = "my_result.csv" The name of the csv file you will like to save your output to, default is pidgin_corpus.csv. (optional parameter)
<br>
News categories include ['nigeria', 'africa', 'sport', 'entertainment']
<br>
removeCategories = [] :as a parameter for news categories you dont want in the scraped corpus. (optional parameter)
e.g , englishCorpus.scrape(noRows = 150, removeCategories = ['entertainment']) 

pass onlyCategories = [] : as a parameter for only categories you want in the scraped corpus. (optional parameter)
e.g , englishCorpus.scrape(noRows = 150, onlyCategories = ['nigeria','sport', 'entertainment'])

```
from anjie import pidginCorpus
pidginCorpus.scrape(noRows = 20)
df = pd.read_csv("pidgin_corpus.csv")
```
  
<b>Scraping Yoruba Corpus</b>
<br>
noRows = 2 The number of rows of news you want.
<br>
csvFileName = "my_result.csv" The name of the csv file you will like to save your output to, default is yoruba_corpus.csv. (optional parameter)
<br>
  
```
from anjie import yorubaCorpus
yorubaCorpus.scrape(noRows = 20)
df = pd.read_csv("yoruba_corpus.csv")
```
  
<b>Installation</b>
Available for install on python >= 3.6

```
$pip install anjie
```
  
Github link for project - https://github.com/Free-tek/Anjie_local_language_corpus_generator 

