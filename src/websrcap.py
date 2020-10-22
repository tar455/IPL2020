import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--DarkReader')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
names=[]
matchs=[]
hss=[]
avgs=[]
strikertaes=[]
f4s=[]
s6s=[]
browser.get("https://www.iplt20.com/stats/2020/most-runs")
content=browser.page_source
soup=BeautifulSoup(content)
for a in soup.findAll('table',attrs={'class':'table table--scroll-on-tablet top-players'}):
    name=a.find('span',attrs={'class':'top-players__last-name'})
    match=a.find('td',attrs={'class':'top-players__m top-players__padded '})
    hs=a.find('td',attrs={'class':'top-players__hs'})
    avg=a.find('td',attrs={'class':'top-players__a'})
    strikerate=a.find('td',attrs={'class':'top-players__sr'})
    f4=a.find('td',attrs={'class':'top-players__4s'})
    s6=a.find('td',attrs={'class':'top-players__6s'})
    names.append(name.text)
    matchs.append(int(0 if match is None else match))
    hss.append(hs)
    avgs.append(avg.text)
    strikertaes.append(strikerate.text)
    f4s.append(f4.text)
    s6s.append(s6.text)
df=pd.DataFrame({'Players Name':names,'Match':matchs,'High score':hss,'average':avgs,'Strike Rate':strikertaes,'4':f4s,'6':s6s})
df.to_csv('C:/Users/hp/Desktop/IPL2020/Data/Batsman.csv', index=False, encoding='utf-8')
