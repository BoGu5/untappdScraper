#!/usr/bin/python3
import bs4
import re 
import requests


bierRegex = re.compile(r'(<a href=\"(\/b\/.*?)\">.*?)(.*?)</a>')

def getBierlist(url):
    bierlist = []
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.find_all('a')
    
    print (type(elems))
    for line in elems:
        bierlist.append(str(line))    
    
    for i in bierlist:
        #if i != None:
        wef = bierRegex.search(i)
        if wef:
            print( 'Nieuw bier gevonden!' + '\n' + wef.group(3) + '\n' 'http://untappd.com/'+ wef.group(2) + '\n') 
        #print(wef.group(1))
        
        
    print(bierlist)    
    #bierlist = 
    #print(bierlist.group)

print('test')

url = 'https://untappd.com/brouwerijpalm/beer?sort=created_at_desc'
getBierlist(url)
