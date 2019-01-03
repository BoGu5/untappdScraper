#!/usr/bin/python3
import bs4
import re 
import requests
import json


brouwerijlijst = ['hetuiltje', 'BrouwerijDeMolen']
#TODO: json bierlijst

#with open("bierlijst.json") as bierlijstfile:
#    bierDict = json.load(bierlijst)

bierRegex = re.compile(r'(<a href=\"(\/b\/.*?)\">.*?)(.*?)</a>')
bierDict = {}

def getBierlist(brouwerij):
    url = 'https://untappd.com/' + brouwerij + '/beer?sort=created_at_desc'
    bierlist = []
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.find_all('a')
    
    #print (type(elems))
    for line in elems:
        bierlist.append(str(line))    
    
    for i in bierlist:
        #if i != None:
        gevonden = bierRegex.search(i)
        if gevonden:
            print( 'Nieuw bier gevonden!' + '\n' + gevonden.group(3) + '\n' 'http://untappd.com'+ gevonden.group(2) + '\n')
            #print(gevonden) 
            bierDict.update({gevonden.group(3): gevonden.group(2)})
        #print(wef.group(1))
        
        
    #print(bierlist)    
    #bierlist = 
    #print(bierlist.group)

print('test')

for brouwerij in brouwerijlijst: 
    getBierlist(brouwerij)
    
print(bierDict)


with open("bierlijst.json",'w') as bierlijstfile:
    json.dump(bierDict, bierlijstfile, indent=2)