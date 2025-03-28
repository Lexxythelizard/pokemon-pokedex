# pokeapi gets the datas from the APIs

import requests

from pokemon_data import (
pokemon_identity_keys, pokemon_physiology_keys, pokemon_stats, pokemon_type_keys
)

pokemon_urls = {
    'get_pokemon': 'https://pokeapi.co/api/v2/pokemon/',
    'get_generation': 'https://pokeapi.co/api/v2/generation/'
}

def get_existing_gens():

    response = requests.get(pokemon_urls['get_generation'])
    if response.status_code == 200:
        try:
            gens = response.json()['count']
        except KeyError:
            gens = f'Data not found. Please check api {pokemon_urls["get_generation"]}'
        return gens


def get_all_pokemon_name_in_gen(gen: int):

    url = f'{pokemon_urls["get_generation"]}{gen}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            name_list = [poke['name'] for poke in response.json()['pokemon_species']]
        except TypeError:
            name_list = ['Missing 1 required positional argument: "gen"']
        except KeyError:
            name_list = ['Failure! Please check the structure of the api data']
    else:
        name_list = ['gen not found. Please check']
    return name_list


def get_pokemon_data(name_or_nr):
    url = f"{pokemon_urls['get_pokemon']}{name_or_nr}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_pokemon_ident(name_or_nr):

    data = get_pokemon_data(name_or_nr)
    if data:
        try:
            identity = {
                pokemon_identity_keys[0]: data['name'],
                pokemon_identity_keys[1]: data['id']
            }
        except ValueError:
            identity = {'NULL': 'some failure happened'}    # wird noch spezifiziert
    else:
        identity = {'NULL': 'API not found. Please check'}
    return identity


def get_pokemon_physiology(name_or_nr):

    data = get_pokemon_data(name_or_nr)
    if data:
        try:
            physiology = {
                pokemon_physiology_keys[0]: data['height'],
                pokemon_physiology_keys[1]: data['weight']
            }
        except ValueError:
            physiology = {'NULL': 'some failure happened'}  # wird noch spezifiziert
    else:
        physiology = {'NULL': 'API not found. Please check'}
    return physiology


def get_pokemon_stats(name_or_nr):

    data = get_pokemon_data(name_or_nr)
    if data:
        try:
            stats = {
                pokemon_stats[key]: stat['base_stat'] for key, stat in enumerate(data['stats'])
            }
        except ValueError:
            stats = {'NULL': 'some failure happened'}  # wird noch spezifiziert
    else:
        stats = {'NULL': 'API not found. Please check'}
    return stats

def get_pokemon_types(name_or_nr):

    data = get_pokemon_data(name_or_nr)
    if data:
        try:
            types = {
                pokemon_type_keys[key]: typ3['type']['name'] for key, typ3 in enumerate(data['types'])
            }
        except ValueError:
            types = {'NULL': 'some failure happened'}  # wird noch spezifiziert
    else:
        types = {'NULL': 'API not found. Please check'}
    return types

