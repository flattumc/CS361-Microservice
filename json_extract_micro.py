from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Assuming your JSON file is named 'pokemon_moves.json' and located in the same directory as this script.
# Adjust the file path as necessary.
JSON_FILE_PATH = 'web/pokemon_moves.json'

def load_pokemon_moves():
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("JSON file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return {}

# Load the JSON data once when the app starts
pokemon_moves = load_pokemon_moves()

@app.route('/pokemon/<pokemon_name>', methods=['GET'])
def get_pokemon_moves(pokemon_name):
    # Retrieve moves for the given Pokémon name
    moves = pokemon_moves.get(pokemon_name.lower())
    
    if moves is not None:
        return jsonify([move['name'] for move in moves])
    else:
        return jsonify({"error": f"Moves for Pokémon '{pokemon_name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
