import urllib.request as urllib2
from bs4 import BeautifulSoup
import lab3
from state import State
import json

req = urllib2.Request('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_flowers', headers={'User-Agent' : "Firefox"})
con = urllib2.urlopen(req)
soup = BeautifulSoup(con)
tags=soup.findAll('img')

states = []
j_data = {}
with open('state_data.json', 'r', encoding="utf-8") as i_file:
    j_data = json.load(i_file)

for s in j_data:
    state = State()
    state.set_name(s['state'])
    state.population = int(s['population'])
    states.append(state)

print(states)
states = lab3.sort_by_name(states)
i = 0
for tag in tags:
    if '/commons/thumb/' in tag['src']:
        print(tag['src'])
        image_data = urllib2.urlretrieve('https:' + tag['src'], 'images/' + states[i].name + '.jpg')
        i += 1
