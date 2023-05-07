import pandas as pd 
import re

												

def number() :
    df = pd.read_csv('/home/abdo/scripts/zumiez/emiratesbd-linkssss.csv')
    return (df['n'].values.tolist())



def links() :
    df = pd.read_csv('/home/abdo/scripts/zumiez/emiratesbd-linkssss.csv')
    return (df['url'].values.tolist())
#for link in links():
    
#    x = re.findall("(?<=of).*[0-9.]+", link)
#    print(*x)
    
for k,l in zip(links() , number()) :
    for i in range (1, ((int(l))+1)):
        print(f"{k}-{i}")