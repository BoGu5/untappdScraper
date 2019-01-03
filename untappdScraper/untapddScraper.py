#!/usr/bin/python3
import bs4
import re 
import requests

bierlist = ''

def getBierlist(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.find_all('a:' )
    print (elems)



url = 'https://untappd.com/brouwerijpalm/beer?sort=created_at_desc'
getBierlist(url)