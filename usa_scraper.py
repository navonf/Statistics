import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import Request, urlopen

base_url = 'https://www.npr.org'
url = 'https://www.npr.org/sections/news/archive?date=1-31-2017'
req = requests.get(url)
data = req.text
soup = BeautifulSoup(data, 'lxml')
div = soup.find('div', class_='year year-2017')
a = div.find_all('a')
links = []
f = open('usanews.txt', 'w')

for i in a:
    links.append(base_url + i['href'])

# links are put in backwards starting at december, this revereses that.
links.reverse()

for link in links:
    link_req = requests.get(link)
    link_data = link_req.text
    link_soup = BeautifulSoup(link_data, 'lxml')
    articles = link_soup.find_all('article', class_='item has-image')
    print("************************************************")
    print(len(articles))
    print("************************************************")
    for i in range(0, 10):
        article_h2 = articles[i].find('h2', class_='title')
        article_link = article_h2.find('a')['href']
        article_req = requests.get(article_link)
        article_data = article_req.text
        article_soup = BeautifulSoup(article_data, 'lxml')
        article_div = article_soup.find_all('div', class_='storytext storylocation linkLocation')
        # print(article_div)
        p = article_div[0].find_all('p')
        story = ''
        for paragraph in p:
            if paragraph.string is None:
                continue
            story = story + paragraph.string

        print(story)

        f.write(story + '\n')
        print("-------------------")

        if 'Hobby Lobby agreed' in story:
            break

        if 'Flooded houses near' in story:
            break

        if 'Los Angeles police officers' in story:
            break
f.close()
