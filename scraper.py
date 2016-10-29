#!venv/bin/python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# example data
raw_data = {'first_name': ['Tom', 'Sam', 'Kate', 'Emma'],
            'last_name': ['Harman', 'Sharman', 'Kharman', 'Eharman']}

# create data frame
raw_df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name'])

# view data frame
print raw_df

# remote data source
url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'
# url = 'http://crackthecode.fiso.co.uk/blog/'

html = requests.get(url)


# make a Beautiful Soup object
soup = BeautifulSoup(html.text, 'lxml')

# vars to temporarily store scraped data
first_name = []
last_name = []

table = soup.find(class_='dataframe')
# table = soup.find(class_='table')

# loop over table rows (skipping the first one)
for row in table.find_all('tr')[1:]:
    col = row.find_all('td')

    col_1 = col[1].string.strip()
    first_name.append(col_1)

    col_2 = col[2].string.strip()
    last_name.append(col_2)

columns = {'first_name': first_name, 'last_name': last_name}

df = pd.DataFrame(columns)

print df