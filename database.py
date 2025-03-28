import sqlite3

from pokemon_data import (
pokemon_identity_keys, pokemon_type_keys, pokemon_stats,
pokemon_physiology_keys, pokemon_gen_key,

DB_NAME, pokemon_table_name, db_column_map
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pokemon_class import Pokemon

# ---------------- database ----------------


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {pokemon_table_name} (
            dex_nr INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type1 TEXT,
            type2 TEXT,
            hp INTEGER,
            attack INTEGER,
            defense INTEGER,
            sp_attack INTEGER,
            sp_defense INTEGER,
            speed INTEGER,
            height INTEGER,
            weight INTEGER,
            gen INTEGER
        )
        """)
        conn.commit()


def insert_pokemon(pkmn: "Pokemon"):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO pokemon (
            dex_nr, name, type1, type2,
            hp, attack, defense, sp_attack, sp_defense, speed,
            height, weight, gen
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            pkmn.ident[pokemon_identity_keys[1]],
            pkmn.ident[pokemon_identity_keys[0]],
            pkmn.types[pokemon_type_keys[0]],
            pkmn.types[pokemon_type_keys[1]],
            pkmn.stats[pokemon_stats[0]],
            pkmn.stats[pokemon_stats[1]],
            pkmn.stats[pokemon_stats[2]],
            pkmn.stats[pokemon_stats[3]],
            pkmn.stats[pokemon_stats[4]],
            pkmn.stats[pokemon_stats[5]],
            pkmn.physiology[pokemon_physiology_keys[0]],
            pkmn.physiology[pokemon_physiology_keys[1]],
            pkmn.gen
        ))
        conn.commit()

def get_stat_from_db(name: str, stat: str) -> int:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT {db_column_map[stat]} FROM pokemon WHERE name = ?", (name,))
        row = cursor.fetchone()
        return row[0] if row else 0


def get_stats_from_db(name: str) -> dict:
    try:
        stats = {
            key: get_stat_from_db(name, stat=key) for key in list(pokemon_stats.values())
        }
    except (TypeError, ValueError):
        stats = {key: 0 for key in list(pokemon_stats.values())}
        print('Sorry something went wrong. Can\'read stats or not not existing :/')
    return stats


def get_two_cells_from_db(name:str, any_keys: dict) ->list:
    with connect() as conn:
        # a, b = any_keys.values()
        a, b = [db_column_map[val] for val in any_keys.values()]
        cursor = conn.cursor()
        cursor.execute(f"SELECT {a}, {b} FROM pokemon WHERE name = ?", (name,))
        row = cursor.fetchone()
        return row


def get_ident_from_db(name: str) -> dict:
    row = get_two_cells_from_db(name=name, any_keys=pokemon_identity_keys)
    return {pokemon_identity_keys[i]: val for i, val in enumerate(row)}


def get_types_from_db(name: str) -> dict:
    row = get_two_cells_from_db(name=name, any_keys=pokemon_type_keys)
    return {pokemon_type_keys[i]: val for i, val in enumerate(row)}


def get_physiology_from_db(name: str) -> dict:
    row = get_two_cells_from_db(name=name, any_keys=pokemon_physiology_keys)
    return {pokemon_physiology_keys[i]: val for i, val in enumerate(row)}


def get_pokemon_gen_from_db(name: str) -> int:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT {pokemon_gen_key[0]} FROM pokemon WHERE name = ?", (name,))
        row = cursor.fetchone()
        return row[0] if row else 0


def get_pokemon_by_name_all_data(name: str) -> dict:
    return {
        "ident": get_ident_from_db(name),
        "types": get_types_from_db(name),
        "stats": get_stats_from_db(name),
        "physiology": get_physiology_from_db(name),
        "gen": get_pokemon_gen_from_db(name),
    }


# --- PERFORMANCE-ALTERNATIVE ---
# hint: should be quick by many calls, but more difficult to maintain.

'''
def get_pokemon_by_name_all_data(name: str) -> dict:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pokemon WHERE name = ?", (name,))

        row = cursor.fetchone()     # fetches the row which was selected by the cursor
        if row:                     # if the row exists
            return {
                'ident': {
                    pokemon_identity_keys[0]: row[1],
                    pokemon_identity_keys[1]: row[0]},
                'types': {
                    pokemon_type_keys[0]: row[2],
                    pokemon_type_keys[1]: row[3]},
                'stats': {
                    pokemon_stats[0]: row[4],
                    pokemon_stats[1]: row[5],
                    pokemon_stats[2]: row[6],
                    pokemon_stats[3]: row[7],
                    pokemon_stats[4]: row[8],
                    pokemon_stats[5]: row[9]},
                'physiology': {
                    pokemon_physiology_keys[0]: row[10],
                    pokemon_physiology_keys[1]: row[11]},
                'gen': row[12]
            }
        return {'NULL': 'This row Entry does not exist.'}
'''
# ------- Performance alternative END

def get_all_stat_values(stat: str) -> list[int]:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT {stat} FROM pokemon")
        return [row[0] for row in cursor.fetchall()]


def get_x_pokemon_data(pokemons: list) -> list:

    try:
        pokemon_data = [get_pokemon_by_name_all_data(pokemon) for pokemon in pokemons]
    except (IndexError, KeyError, ValueError):
        pokemon_data = ['Failure: something went wrong :/']
    return pokemon_data