from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())


def getLinks(articleURL):

    html = urlopen('https://en.wikipedia.org{}'.format(articleURL))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))


def main():

    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) > 0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)

main()
