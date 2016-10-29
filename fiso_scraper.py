#!venv/bin/python
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

# remote data source
url = 'http://crackthecode.fiso.co.uk/blog/'


def get_price_changes():
    html = requests.get(url)

    # make a Beautiful Soup object
    soup = BeautifulSoup(html.text, 'lxml')

    # vars to temporarily store scraped data
    player_name = []
    position = []
    team = []
    price = []
    ownership = []
    net_transfers_in = []
    target_percentage = []

    table = soup.find(class_='table')

    # loop over table rows (skipping the first one)
    for row in table.find_all('tr')[1:]:
        col = row.find_all('td')

        col_1 = col[1].string.strip()
        player_name.append(col_1)

        col_2 = col[2].string.strip()
        position.append(col_2)

        col_3 = col[3].string.strip()
        team.append(col_3)

        col_4 = col[4].string.strip()
        price.append(col_4)

        col_5 = col[5].string.strip()
        ownership.append(col_5)

        col_6 = col[6].string.strip().replace(',', '')
        net_transfers_in.append(int(col_6))

        col_7 = col[7].string.strip()
        target_percentage.append(float(col_7))

    columns = {'player_name': player_name,
               'position': position,
               'team': team,
               'price': price,
               'ownership': ownership,
               'net_transfers_in': net_transfers_in,
               'target_percentage': target_percentage}

    df = pd.DataFrame(columns)

    # arrange by transfers in
    # print df.sort_values(by='net_transfers_in')
    most_likely_players_to_rise_in_price = df.sort_values(by='target_percentage').tail()
    to_json = most_likely_players_to_rise_in_price.to_json(orient='records')
    parsedAsPyObj = json.loads(to_json)
    return parsedAsPyObj
    # return json.dumps(parsedAsPyObj, indent=4)
    # print df.head()
