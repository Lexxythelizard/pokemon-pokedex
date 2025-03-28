# 🧬 Pokémon Pokédex (Python & SQLite)

This is a modular and expandable Pokédex app, written in Python, using the [PokéAPI](https://pokeapi.co/) and a local SQLite database.  
You can fetch Pokémon data from the API, store it locally, and retrieve it at any time — your own mini Pokédex! 🌿📦

---

## 🔧 Features

- ✅ Fetch Pokémon data from the PokéAPI (stats, types, height, etc.)
- ✅ Store data in a local SQLite database (`pokedex.db`)
- ✅ Retrieve data from the database and display it
- ✅ Object-oriented structure using a `Pokemon` class
- ✅ Fully modular codebase: API, DB, data, logic separated
- ✅ Dynamic key mapping for flexibility and maintainability

---

## 🗃️ Tech Stack

- **Python 3.10+**
- `requests` for HTTP communication
- `sqlite3` for local storage
- Modular files for separation of concerns

---

## 📁 Project Structure
```
pokemon_pokedex/ 
├── main.py # Entry point, test runner 
├── pokemon_class.py # Main class: Pokemon 
├── pokeapi.py # API access logic 
├── database.py # SQLite database logic 
├── pokemon_data.py # Centralized key & data definitions 
├── pokedex.db # SQLite database (created automatically) 
├── README.md # English project description 
└── README_DE.md # (optional) German version
```
## ✨ Highlights

- Dynamic Mapping: internal keys <-> DB column names
- Error handling & fallback mechanisms
- Fully modularized and easy to extend
- Local data storage – works without internet

## ⚛️ Planned for Version 2

- GUI with Tkinter
- Search & filter functions
- Data analysis (averages, distributions, etc.)
- Expandability for additional generations & attributes

## 👤 Credits

Project by Lenina aka Lexxythelizard
Start: March 23, 2025 – Goal: Learn, build & understand
Special thanks to: Vera F. Birkenbihl, morning fog & the tiny pocket monsters ;) 🧩

---

## 🚀 Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Lexxythelizard/pokemon-pokedex.git
   cd pokemon-pokedex
