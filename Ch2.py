'''
< span class =" red" > Heavens! what a virulent attack! </ span >replied
< span class =" green" > the prince </ span >, not in the least disconcerted by this reception.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)