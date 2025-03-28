# pokemon-data and keys

# This Module contains just Data and keys.
# So almost every change could be centralized.

# Keys for Pokemon-class

pokemon_stats = {
    0: 'hp', 1: 'attack', 2: 'defense', 3: 'special-attack', 4: 'special-defense', 5: 'speed'
}
pokemon_stats_invert = {val: key for key, val in pokemon_stats.items()}

pokemon_identity_keys = {0: 'name', 1: 'dex nr'}
pokemon_physiology_keys = {0: 'height', 1: 'weight'}
pokemon_type_keys = {0: 'type 1', 1: 'type 2'}
pokemon_gen_key = {0: 'gen'}

gens_existing = 9

# ----------- database.py keys and strings --------------

DB_NAME = "pokedex.db"
pokemon_table_name = "pokemon"

# Mapping von internen Keys auf DB-Spaltennamen
db_column_map = {
    pokemon_identity_keys[0]: 'name',
    pokemon_identity_keys[1]: 'dex_nr',
    pokemon_type_keys[0]: 'type1',
    pokemon_type_keys[1]: 'type2',
    pokemon_stats[0]: 'hp',
    pokemon_stats[1]: 'attack',
    pokemon_stats[2]: 'defense',
    pokemon_stats[3]: 'sp_attack',
    pokemon_stats[4]: 'sp_defense',
    pokemon_stats[5]: 'speed',
    pokemon_physiology_keys[0]: 'height',
    pokemon_physiology_keys[1]: 'weight',
    pokemon_gen_key[0]: 'gen'
}

