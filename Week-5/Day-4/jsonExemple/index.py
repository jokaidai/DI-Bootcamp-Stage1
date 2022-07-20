import json
from pprint import pprint
from random import choice

with open("./file.json", mode = 'r') as f:
    family = json.load(f)

pprint(family['children'])

print (" ------------- ")

colors = ['red', 'blue', 'yellow', 'green', 'white', 'black']
for child in family['children']:
    rand_color = choice(colors)
    child['favorite_color'] = rand_color

pprint(family)

with open("./file.json", mode = 'w') as f:
    family = json.dump(family, f, indent = 2, sort_keys = True)