from flask import Flask, render_template, request, jsonify
from game import Game

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    game.initialise_game() 
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():

    state = game.load_game_state_from_db()
    return jsonify({
        'output': game.get_state_text(state) # Assuming game_state has a to_dict method
    })
    # data = request.get_json()
    # player_move = data.get('move')


    # game.play_move(player_move)

    
    # state = game.load_game_state_from_db()

    # if state.game_status() == 1:
    #     return jsonify({
    #         'status': 'game_over',
    #         'message': 'You win!'
    #     })
    # else:
    #     return None
    

    # # Get updated state
    # state_text = game.get_state_text()
    # return jsonify({
    #     'state': state_text,
    #     'num_rollouts': game.num_rollouts,
    #     'search_time': game.search_time
    # })

if __name__ == '__main__':
    app.run(debug=True)