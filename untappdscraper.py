#!/usr/bin/python3
import bs4
import re 
import requests
import json
import telegram_send
import html
import time


brouwerijlijst = ['hetuiltje', 'BrouwerijDeMolen', 'BierbrouwerijEmelisse', 'BrouwerijKees', 'jopen']

bierRegex = re.compile(r'(<a href=\"(\/b\/.*?)\">.*?)(.*?)</a>')
bierDict = {}
bierList = []
bierString = ""

#telegram_send.configure('~/.config/telegram-send.conf')

try:
    with open("bierlijst.json") as bierlijstfile:
        bierDict = json.load(bierlijstfile)
except OSError:
    pass

def checkBierNieuw(bier, link):
    if bier not in bierDict.keys():
        #print('Nieuw bier gevonden!' + '\n' + bier + '\n' 'http://untappd.com'+ link + '\n')
        bierList.append(html.unescape('*Nieuw bier gevonden!*' + '\n_' + bier + '_\n' 'http://untappd.com'+ link + '\n')) 
        bierDict.update({bier:link})

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
            #print( 'Nieuw bier gevonden!' + '\n' + gevonden.group(3) + '\n' 'http://untappd.com'+ gevonden.group(2) + '\n')
            #print(gevonden) 
            #bierDict.update({gevonden.group(3): gevonden.group(2)})
            checkBierNieuw(gevonden.group(3), gevonden.group(2))

for brouwerij in brouwerijlijst: 
    getBierlist(brouwerij)
    time.sleep(60)

#bierString = '\n'.join(bierList)
#bierString = html.unescape(bierString)

telegram_send.send(messages=bierList, parse_mode="markdown")

print(bierString)    

with open("bierlijst.json",'w') as bierlijstfile:
    json.dump(bierDict, bierlijstfile, indent=2)
