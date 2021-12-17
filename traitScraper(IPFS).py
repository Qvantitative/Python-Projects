## Import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import ast

start_time = time.time()
s = requests.Session()

## Get URL and extract content
page=1
traits = []
fur = []

while page != 100:

    params = {
               ## TokenURI Address
        ('arg', f"QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/{page}"),
    }

    content = s.get('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=('20IHRX1V04tTEaBPuLRBRmzNQ3d', '0e82f1926a694e984a70519d37227247'))
    soup = BeautifulSoup(content.text, 'html.parser')
    page = page + 1

    traits = ast.literal_eval(soup.text)['attributes']

    df = pd.DataFrame(traits)
    df1 = df[df['trait_type']=='Fur']

    try:
        fur.append(df1['value'].to_numpy()[0])
    except:
        fur.append('NONE')

a = pd.DataFrame({'Fur': fur})
value_counts1 = a['Fur'].value_counts()
amount = [f"{key}, {value_counts1[key]}" for key in value_counts1.keys()]
#amount = [f"{key}, {tokenID}, {value_counts1[key]}" for key in value_counts1.keys()]

ax = pd.DataFrame(
    amount, columns=['Fur'])

## Select specific traits
a1 = a[a['Fur']=='Robot']
a2 = a[a['Fur']=='Zombie']

## Attach a2 -> a2
ay = a1.append(a2)
ay.reset_index(level=0, inplace=True)

## Select index column
az = ay['index']

#ay.to_csv(r'C:/Users/miked/OneDrive/Desktop/scraper/traitScraper(IPFS).csv', index=False)
print("--- %s seconds ---" % (time.time() - start_time))