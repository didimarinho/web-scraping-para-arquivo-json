import pandas as pd
import requests
from bs4 import BeautifulSoup



url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')

tablebank = soup.find('table')


df = pd.read_html(str(tablebank), header=0)[0]


df.to_json('banks.json', orient='records', indent=4)


