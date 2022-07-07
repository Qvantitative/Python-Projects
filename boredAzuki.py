#Import Library
from web3 import Web3
import pandas as pd
import json
import time
from ens import ENS

start_time = time.time()

i=1

addressesGrillz = []
addressesAzuki = []
addressesBAYC = []
ensAzuki =[]
ensBAYC = []

#Connect to INFURA HTTP End Point
infura_url='https://mainnet.infura.io/v3/25a5624883354bdeaf467ca41cf912de' #your uri
w3 = Web3(Web3.HTTPProvider(infura_url))

#Check Connection
w3.isConnected()

ns = ENS.fromWeb3(w3)
#abiBAYC="http://api.etherscan.io/api?module=contract&action=getabi&address=0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d&format=raw"
#abiBAYC = requests.get(abiBAYC).json()

with open('C:/Users/miked/OneDrive/Desktop/scraper/contracts/azuki.json') as json_file:
    dataAzuki = json.load(json_file)

with open('C:/Users/miked/OneDrive/Desktop/scraper/contracts/BAYC.json') as json_file:
    dataBAYC = json.load(json_file)

addressAzuki = "0xed5af388653567af2f388e6224dc7c4b3241c544"
addressBAYC = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

addressAzuki = Web3.toChecksumAddress(addressAzuki)
addressBAYC = Web3.toChecksumAddress(addressBAYC)

contractAzuki = w3.eth.contract(address=addressAzuki, abi=dataAzuki)
contractBAYC = w3.eth.contract(address=addressBAYC, abi=dataBAYC)

while i != 10000:
    try:
        ownerAzuki = contractAzuki.functions.ownerOf(i).call()
        ownerBAYC = contractBAYC.functions.ownerOf(i).call()
    except:
        pass
    
    i = i + 1
    
    ensAzuki.append(ns.name(ownerAzuki))
    ensBAYC.append(ns.name(ownerBAYC))
    addressesAzuki.append(ownerAzuki)
    addressesBAYC.append(ownerBAYC)
    
a = pd.DataFrame({'Address Count': ensAzuki})
b = pd.DataFrame({'Address Count': ensBAYC})

aa = pd.DataFrame({'Address Count': addressesAzuki})
bb = pd.DataFrame({'Address Count': addressesBAYC})

c = aa.merge(bb, on=['Address Count'])

aaa = a.combine_first(aa)
bbb = b.combine_first(bb)

cc = aaa.merge(bbb, on=['Address Count'])

value_counts1 = aaa['Address Count'].value_counts()
value_counts2 = bbb['Address Count'].value_counts()
value_counts3 = cc['Address Count'].value_counts()

l1 = [f"{key}" for key in value_counts3.keys()]
l2 = [f"{value_counts2[key]}" for key in value_counts3.keys()]
l3 = [f"{value_counts1[key]}" for key in value_counts3.keys()]

holders = l1, l2, l3

dfx = pd.DataFrame(
    holders, index=['Wallets', 'BAYC Count', 'Azuki Count'])

dfx = dfx.T

dfx.to_csv(r'C:/Users/miked/OneDrive/Desktop/scraper/boredAzuki.csv', index=False)

print("--- %s seconds ---" % (time.time() - start_time))