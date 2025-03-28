# Pokémon Pokedex

**Version 1 – Stable Pokédex MVP**  
_Ein eigener, lokal gespeicherter Pokédex!_

---

## 🐉 Features

- Pokémon-Daten werden direkt aus der **PokéAPI** geladen
- Speicherung in einer lokalen **SQLite-Datenbank**
- Objektorientierte Struktur mit **modularer Architektur**:
  - `pokemon_class.py`: Zentrale `Pokemon`-Klasse
  - `pokeapi.py`: Zugriff auf die PokéAPI
  - `database.py`: Speicherung & Abfrage per SQLite
  - `pokemon_data.py`: zentrale Daten- und Keyverwaltung
- Komplette Datensätze können geladen, gespeichert und wieder abgerufen werden

---

## 🗃️ Tech Stack

```
python
- **Python 3.10+**
- `requests` for HTTP communication
- `sqlite3` for local storage
- Modular files for separation of concerns

```

---

## 📊 Projektstruktur

```
pokemon_pokedex/
├── main.py                  # Test und Demo-Startpunkt
├── pokemon_class.py        # OOP: Pokemon-Klasse
├── pokeapi.py              # Zugriff auf PokéAPI
├── database.py             # SQLite-Speicherung
├── pokemon_data.py         # Zentrale Key-Verwaltung
├── pokedex.db              # Lokale SQLite-Datenbank
```

---

## ✨ Highlights

- Dynamisches Mapping: interne Keys <-> DB-Spaltennamen
- Fehlerbehandlung & Fallbacks
- Voll modularisiert, einfach zu erweitern
- Lokale Speicherung unabhängig von Internet

---

## ⚛️ Geplant für Version 2

- GUI mit Tkinter
- Suche & Filterfunktionen
- Datenanalyse (Durchschnittswerte, Verteilungen, etc.)
- Erweiterbarkeit für weitere Generationen & Eigenschaften

---

## 👤 Credits

Projekt von **Lenina aka Lexxythelizard**  
Start: 23. März 2025 – Ziel: Lernen, Bauen & Verstehen  
Special thanks to: Vera F. Birkenbihl, Frühnebel & den kleinen Taschenmonstern ;) 🧩

---

## ✨ Los geht's!

```bash
# Klonen
git clone https://github.com/Lexxythelizard/pokemon-pokedex.git
cd pokemon_pokedex

# Python ausführen
python main.py
```

Enjoy your journey, Trainer! 🏃‍♀️🌿

