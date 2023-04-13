import requests
import pandas
from bs4 import BeautifulSoup
response= requests.get("https://m.imdb.com/news/tv/?ref_=nv_nw_tv")
# print(response)
soup = BeautifulSoup(response.content,'html.parser')
# print(soup)
headlines= soup.find_all('h2',class_='news-item__headline')
names=[]
for i in headlines[0:10]:
    d=i.get_text()
    names.append(d)
# print(names)

newsdate= soup.find_all('li',class_='ipl-inline-list__item')
date=[]
for i in newsdate[0:10]:
    d=i.get_text()
    date.append(d)
# print(date)

images= soup.find_all('img',class_='news-item__image')
img=[]
for i in images[0:10]:
    d= i['src']
    img.append(d)
# print(img)
df=pandas.DataFrame()
# print(df)s
df['headlines']=names
df['newsdate']=date
df['images']=img
# print(df)
df.to_csv('IMb_news.csv')


# df= pandas.DataFrame()
# df['headlines']= hdname
# df['hyperlinks']= links
# print(df)