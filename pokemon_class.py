import pokeapi
import database

from pokemon_data import (
pokemon_stats, pokemon_stats_invert, pokemon_identity_keys,
pokemon_physiology_keys, pokemon_type_keys, pokemon_gen_key,
gens_existing
)

# ---------------- classes ----------------

class Pokemon:

    method_keys = {0: 'ident', 1: 'types', 2: 'stats', 3: 'pysiology'}

    def __init__(self, name='zero', dex_nr=0, gen=0):
        self.ident = {'name': name, 'dex nr': dex_nr}
        self.stats = {stat: 0 for stat in pokemon_stats.values()}
        self.physiology = {'height': 0, 'weight': 0}
        self.types = {type_key : 'NULL' for type_key in pokemon_type_keys.values()}
        self.gen = gen

    def set_ident(self, identity: dict):

        for ident, val in identity.items():
            if ident in self.ident:
                self.ident[ident] = val
            else:
                return f'Key failure: "{ident}" is not valid!\nPlease use: {pokemon_identity_keys}'

    def set_types(self,types: dict):

        for typ3, val in types.items():
            if typ3 in self.types:
                self.types[typ3] = val
            else:
                return f'Key failure: "{typ3}" is not valid!\nPlease use: {pokemon_type_keys}'

    def set_stats(self, stats: dict):

        for stat, val in stats.items():
            if stat in pokemon_stats.values():
                self.stats[stat] = val

    def set_pysiology(self, physio: dict):

        for phy, val in physio.items():
            if phy in self.physiology.keys():
                self.physiology[phy] = val

    def set_gen(self, gen=0):
        if isinstance(gen, int) and not isinstance(gen, bool):
            if 0 < gen <= gens_existing:
                self.gen = gen
            elif not 0 <= gen <= gens_existing:
                self.gen = gen
                return f'Warning! Gen {gen} probably not existing!'
            else:
                # In Zukunft: automatische Gen-Zuweisung aus dex_nr oder so
                pass
        else:
            return 'Type Error! Expected integer.'

    def set_x(self, key: str, argument: dict):

        if key not in self.method_keys.values():
            return f'sorry not wrong key: valid keys are:\n{list(self.method_keys.values())}'

        setting_map = {
            self.method_keys[0]: self.set_ident,
            self.method_keys[1]: self.set_types,
            self.method_keys[2]: self.set_stats,
            self.method_keys[3]: self.set_pysiology
        }
        setting_map[key](argument)

    def from_api(self, key: str, name_or_nr):

        pokeapi_map = {
            self.method_keys[0]: pokeapi.get_pokemon_ident,
            self.method_keys[1]: pokeapi.get_pokemon_types,
            self.method_keys[2]: pokeapi.get_pokemon_stats,
            self.method_keys[3]: pokeapi.get_pokemon_physiology
        }
        self.set_x(
            key=key,
            argument=pokeapi_map[key](name_or_nr)
        )

    def from_database(self, key: str, name_or_nr):

        poke_database_map = {
            self.method_keys[0]: database.get_ident_from_db,
            self.method_keys[1]: database.get_types_from_db,
            self.method_keys[2]: database.get_stats_from_db,
            self.method_keys[3]: database.get_physiology_from_db
        }
        try:
            self.set_x(
                key=key,
                argument=poke_database_map[key](name_or_nr)
            )
        except KeyError:
            return f'seems this method or database.py are still under construction'

    @classmethod
    def from_api_full(cls, name_or_number):
        new_pokemon = cls(name_or_number)
        for key in cls.method_keys.values():
            new_pokemon.from_api(key=key, name_or_nr=name_or_number)
        return new_pokemon

    @classmethod
    def from_database_full(cls, name_or_number: str):
        new_pokemon = cls(name_or_number)
        for key in cls.method_keys.values():
            try:
                new_pokemon.from_database(key=key, name_or_nr=name_or_number)
            except (KeyError, TypeError):
                return f'Still under construction :/\nthanks for your patients ;)'
        return new_pokemon