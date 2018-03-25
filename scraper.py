import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import Request, urlopen

url = 'http://www.euronews.com/2017/'
base_url = 'http://www.euronews.com'
# req = requests.get(url)
# data = req.text
# soup = BeautifulSoup(data, 'lxml')
f = open('euronews.txt', 'w')

for month in range(1, 13):
    for day in range(1, 11):
        temp = url
        if month < 10:
            if day == 10:
                url = url + '0' + str(month) + '/' + str(day)
            else:
                url = url + '0' + str(month) + '/0' + str(day)
        else:
            if day == 10:
                url = url + str(month) + '/' + str(day)
            else:
                url = url + str(month) + '/0' + str(day)

        print(url)
        req = requests.get(url)
        data = req.text
        soup = BeautifulSoup(data, 'lxml')

        a = soup.find_all('a', class_='media__body__link', rel='bookmark')
        article_url = base_url + a[2]['href']
        article_req = requests.get(article_url)
        article_data = article_req.text
        article_soup = BeautifulSoup(article_data, 'lxml')

        section = article_soup.find('div', class_="column small-12 medium-10 xlarge-11 js-responsive-iframes-container")

        # if video comes before text
        if section is None:
            section = article_soup.find('div', class_="u-margin-bottom-2")
            p = section.find_all('p')
        else:
            p = section.find_all('p')

        text = ''
        for s in p:
            reg = re.findall(r'>(.+?)<', str(s))
            if 'class=' in str(reg):
                continue

            if 'src=' in str(reg):
                continue

            if '<span>' in str(reg):
                continue

            if 'pic.twitter.com' in str(reg):
                continue

            if 'https' in str(reg):
                continue

            for r in reg:
                text = text + r
        print(text)
        print('-------------------------------------------------------------------------')
        f.write(text + '\n')
        url = temp

f.close()
