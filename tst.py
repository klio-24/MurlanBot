from game import Game
from MurlanState import game_state
import json

# Create a Game instance
game = Game()

# Load saved state from file (you've saved it locally from DynamoDB)
with open('jsontest.json', 'r') as f:
    saved_state_dict = json.load(f)

# Deserialize to a game_state object
state = game_state.from_dict(saved_state_dict)

# Inject it into the Game instance by saving it to the DB (in-memory version)
game.save_game_state_to_db(state)

# Test a move (e.g., player move)
# Replace with a valid input index depending on the state
game.play_move("1")

# Then test bot's response
game.bot_play_a_turn()

# Check new state and output
new_state = game.load_game_state_from_db()
print(game.get_state_text(new_state))