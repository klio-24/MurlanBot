from flask import Flask, render_template, request, jsonify
from game import Game  # You'll create this simple class

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    player_move = data.get('move')
    game.save_to_db(player_move)
    result = game.play_move(player_move)
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True)