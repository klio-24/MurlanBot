from flask import Flask, render_template, request, jsonify
from game import Game

app = Flask(__name__)
game = Game()

# testing CICD process - this comment should show on main branch...

@app.route('/')
def index():
    game.initialise_game()
    state = game.load_game_state_from_db()
    state_text = game.get_state_text(state)
    return render_template('index.html', state_text=state_text)

@app.route('/move', methods=['POST'])
def move():

    data = request.get_json()
    player_move = data.get('move')

    print("test")
    game.play_move(player_move)

    

    if game.game_status() == 1:
        return jsonify({
            'output': "You win!"
        })

    game.bot_play_a_turn()

    print("bot played a turn")
    if game.game_status() == 2:
        return jsonify({
            'output': "You lose!"
        })
    
    return jsonify({
        'output': game.get_state_text(game.load_game_state_from_db()) 
        })

if __name__ == '__main__':
    app.run(debug=True)