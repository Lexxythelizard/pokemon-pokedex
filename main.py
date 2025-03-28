# pokemon pokedex

import pokeapi
import database
from pokemon_data import pokemon_identity_keys
from pokemon_class import Pokemon

programmers_name = 'Lexxy'

# ----------- motivation -------------

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}!\n\tYou can do it! :)')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(programmers_name)

    print('\nLets check if everything is all right:')
    print(pokeapi.get_existing_gens())
    print(pokeapi.get_all_pokemon_name_in_gen(1))
    print('\nand the get_pokemon_... functions :)')
    print(pokeapi.get_pokemon_ident(4))
    print(pokeapi.get_pokemon_types(4))
    print(pokeapi.get_pokemon_physiology(4))
    print(pokeapi.get_pokemon_stats(4))
    # and now: die Zuweisungen :)
    glu_hu_mandaaa = Pokemon.from_api_full(4)
    print(glu_hu_mandaaa)
    print(
        f'\n{glu_hu_mandaaa.ident}'
        f'\n{glu_hu_mandaaa.types}'
        f'\n{glu_hu_mandaaa.stats}'
        f'\n{glu_hu_mandaaa.physiology}'
    )
    print(f'\nand now we try the SQLite stuff :)')
    database.create_table()
    database.insert_pokemon(glu_hu_mandaaa)
    print(f'\nsuccessfully added to the table :)')


    glu_hu_mandaaa_from_db = Pokemon.from_database_full("charmander")
    print("\n And now call the datas from the data table:")
    print(f"Name: {glu_hu_mandaaa_from_db.ident[pokemon_identity_keys[0]]}")
    print(f"Typen: {glu_hu_mandaaa_from_db.types}")
    print(f"Stats: {glu_hu_mandaaa_from_db.stats}")
    print(f"Größe/Gewicht: {glu_hu_mandaaa_from_db.physiology}")

    print(f'\nnow we compare if they\'re equal :)')
    print(glu_hu_mandaaa.__dict__)
    print(glu_hu_mandaaa_from_db.__dict__)

