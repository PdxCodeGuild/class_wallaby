from flask import Flask, render_template, request
import requests


poke15 = {
    "count": "1118",
    "next": "https://pokeapi.co/api/v2/pokemon?offset=15&limit=15",
    "previous": "null",
    "results": [
        {
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon/1/"
        },
        {
            "name": "ivysaur",
            "url": "https://pokeapi.co/api/v2/pokemon/2/"
        },
        {
            "name": "venusaur",
            "url": "https://pokeapi.co/api/v2/pokemon/3/"
        },
        {
            "name": "charmander",
            "url": "https://pokeapi.co/api/v2/pokemon/4/"
        },
        {
            "name": "charmeleon",
            "url": "https://pokeapi.co/api/v2/pokemon/5/"
        },
        {
            "name": "charizard",
            "url": "https://pokeapi.co/api/v2/pokemon/6/"
        },
        {
            "name": "squirtle",
            "url": "https://pokeapi.co/api/v2/pokemon/7/"
        },
        {
            "name": "wartortle",
            "url": "https://pokeapi.co/api/v2/pokemon/8/"
        },
        {
            "name": "blastoise",
            "url": "https://pokeapi.co/api/v2/pokemon/9/"
        },
        {
            "name": "caterpie",
            "url": "https://pokeapi.co/api/v2/pokemon/10/"
        },
        {
            "name": "metapod",
            "url": "https://pokeapi.co/api/v2/pokemon/11/"
        },
        {
            "name": "butterfree",
            "url": "https://pokeapi.co/api/v2/pokemon/12/"
        },
        {
            "name": "weedle",
            "url": "https://pokeapi.co/api/v2/pokemon/13/"
        },
        {
            "name": "kakuna",
            "url": "https://pokeapi.co/api/v2/pokemon/14/"
        },
        {
            "name": "beedrill",
            "url": "https://pokeapi.co/api/v2/pokemon/15/"
        }
    ]
}

app = Flask(__name__)

url = "https://pokeapi.co/api/v2/pokemon?limit=150"
payload = {}
headers = {}



@app.route('/')
def index():
  response = requests.request("GET", url, headers=headers, data=payload)

  results = response.json()
#   print(results)
  return render_template('index.html', pokemons = results['results'])

@app.route('/pokemon', methods=['POST'])
def pokemon():
    url = f'https://pokeapi.co/api/v2/pokemon/{request.form["pokemon"]}'
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    name = data['name']
    abilities = data['abilities']
    height = data['height']
    weight = data['weight']
    id = data['id']
    moves = data['moves']
    sprite = data['sprites']['front_default']
    stats = data['stats']
    types = data['types']

    tempList = []
    for move in moves:
        tempList.append(move['move']['name'])
    moves = tempList

    tempObj = {}
    for stat in stats:
        tempObj[stat['stat']['name']] = stat['base_stat']
    stats = tempObj
    print('newStats', stats)

    return render_template('profile.html', name = name, height = height, weight = weight, id = id, moves = moves, sprite = sprite, stats = stats, types = types)


if __name__ == '__main__':
  app.run(debug=True)
