from flask import Flask, render_template, request, jsonify
from game import Game

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    game.initialise_game()  # sets up deck, hands, etc.
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    player_move = data.get('move')

    # Validate and process the player's move
   #valid = game.validate_move(player_move)
   #if not valid:
        #return jsonify({'error': 'Invalid move'}), 400

    # Update game state with player move
    game.play_move(player_move)

    # Bot calculates and plays its move (if game not over)
    if not game.is_game_over():
        game.bot_move()

    # Get updated state
    state_text = game.get_state_text()
    return jsonify({
        'state': state_text,
        'num_rollouts': game.num_rollouts,
        'search_time': game.search_time
    })

if __name__ == '__main__':
    app.run(debug=True)