# Import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import ast
import time

start_time = time.time()
s = requests.Session()

page = 1
traits_e = []
backgrounds, class1, race, mha, fha = [], [], [], [], []
#, clothes, heads, mouths = [], [], [], [], [], []

#Get URL and extract content
while page != 500:
    content = s.get('https://img.feudalz.io/{}'.format(page))
    soup = BeautifulSoup(content.text, 'html.parser')
    page = page + 1

    traits = ast.literal_eval(soup.text)['attributes']

    df = pd.DataFrame(traits)
    
    try:
        df1 = df[df['trait_type']=='Background']
        df2 = df[df['trait_type']=='Class']
        df3 = df[df['trait_type']=='Race']
        df4 = df[df['trait_type']=='Male Head Accessory']
        df5 = df[df['trait_type']=='Female Head Accessory']
        mha.append(df5['value'].values[0])
        fha.append(df5['value'].values[0])
    except:
        pass

#    df6 = df[df['trait_type']=='Mouth']
#    dfTC = len(pd.DataFrame(traits).set_index('value').to_numpy())

    backgrounds.append(df1['value'].values[0])
    class1.append(df2['value'].values[0])
    race.append(df3['value'].values[0])
    
#    mouths.append(df6['value'].values[0])
#    traits_e.append(dfTC)
    
a, b, c = pd.DataFrame({'Backgrounds': backgrounds}), pd.DataFrame({'Class': class1}), pd.DataFrame({'Race': race})
d, e = pd.DataFrame({'Male Head Accessory': mha}), pd.DataFrame({'Female Head Accessory': fha})
#, pd.DataFrame({'Mouths': mouths})
#g = pd.DataFrame({'Trait Count': traits_e})

value_counts1 = a['Backgrounds'].value_counts()
value_counts2 = b['Class'].value_counts()
value_counts3 = c['Race'].value_counts()
value_counts4 = d['Male Head Accessory'].value_counts()
value_counts5 = e['Female Head Accessory'].value_counts()
#value_counts6 = f['Mouths'].value_counts()
#value_counts7 = g['Trait Count'].value_counts()

l1, l2 = [f"{key} - {value_counts1[key]}" for key in value_counts1.keys()], [f"{key} - {value_counts2[key]}" for key in value_counts2.keys()]
l3 = [f"{key} - {value_counts3[key]}" for key in value_counts3.keys()]
l4, l5 = [f"{key} - {value_counts4[key]}" for key in value_counts4.keys()], [f"{key} - {value_counts5[key]}" for key in value_counts5.keys()]
#, [f"{key} - {value_counts6[key]}" for key in value_counts6.keys()]
#l7 = [f"{key} - {value_counts7[key]}" for key in value_counts7.keys()]

traits1 = l1, l2, l3, l4, l5
#, l6, l7

dfx = pd.DataFrame(
    traits1, index=['Background', 'Class', 'Race', 'Male Head Accessory', 'Female Head Accessory'])

#dfx = dfx.T
#dfx.to_csv(r'C:/Users/miked/OneDrive/Desktop/scraper/nftScraper.csv', index=False)

#print(dfx)
#print("--- %s seconds ---" % (time.time() - start_time))