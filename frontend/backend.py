


from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Создаем карту 20x20 и устанавливаем начальное положение персонажа
MAP_SIZE = 20
character_position = [random.randint(0, MAP_SIZE-1), random.randint(0, MAP_SIZE-1)]

def generate_map():
    # Генерируем пустую карту
    game_map = [['.' for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    # Устанавливаем персонажа на карту
    game_map[character_position[0]][character_position[1]] = 'P'
    return game_map

@app.route("/get_map", methods=["GET"])
def get_map():
    game_map = generate_map()
    return jsonify({"map": game_map})

@app.route("/move_character", methods=["POST"])
def move_character():
    direction = request.json["direction"]
    if direction == "up":
        if character_position[0] > 0:
            character_position[0] -= 1
    elif direction == "down":
        if character_position[0] < MAP_SIZE - 1:
            character_position[0] += 1
    elif direction == "left":
        if character_position[1] > 0:
            character_position[1] -= 1
    elif direction == "right":
        if character_position[1] < MAP_SIZE - 1:
            character_position[1] += 1
    game_map = generate_map()
    return jsonify({"map": game_map})

if __name__ == "__main__":
    app.run(debug=True)

