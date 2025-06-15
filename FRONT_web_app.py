from flask import Flask, render_template, request, jsonify
from BACK_game import Game  # You'll create this simple class

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST']) # 'start' endpoint to handle starting a new game
def start_game():
    game.start_new_game()
    return jsonify({'status': 'Game started', 'session_id': game.session_id})

if __name__ == '__main__':
    app.run(debug=True)