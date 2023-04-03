from pprint import pprint

import requests

URL = 'https://akabab.github.io/superhero-api/api/all.json'

res = requests.get(URL)
heroes = res.json()


our_heroes = {}

for hero in heroes:
    if hero['name'] in ['Hulk','Captain America', 'Thanos']:
        our_heroes = {hero['name']:hero['powerstats']['intelligence']}

print(max(our_heroes, key=our_heroes.get))
