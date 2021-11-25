import requests
from bs4 import BeautifulSoup
import sys



headers = {'User-Agent': 'Mozilla/5.0'}
urls="https://anapioficeandfire.com/api/books/1"

r = requests.get(urls, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup)
