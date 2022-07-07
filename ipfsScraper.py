# Import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import ast

start_time = time.time()
s = requests.Session()

#Get URL and extract content
page=1
traits = []
backgrounds = []

while page != 2:

    params = {
        ('arg', f"Qmer3VzaeFhb7c5uiwuHJbRuVCaUu72DcnSoUKb1EvnB2x/{page}"),
    }
    
    content = s.get('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=('20IHRX1V04tTEaBPuLRBRmzNQ3d', '0e82f1926a694e984a70519d37227247'))
    soup = BeautifulSoup(content.text, 'html.parser')
    page = page + 1

    traits = ast.literal_eval(soup.text)['attributes']

    df = pd.DataFrame(traits)
    df1 = df[df['trait_type']=='BACKGROUND']

    backgrounds.append(df1['value'].values[0])

a = pd.DataFrame({'BACKGROUND': backgrounds})
value_counts1 = a['BACKGROUND'].value_counts()
l1 = [f"{key} - {value_counts1[key]}" for key in value_counts1.keys()]
t = l1

dfx = pd.DataFrame(
    t, columns=['BACKGROUND'])

print(dfx)
print("--- %s seconds ---" % (time.time() - start_time))