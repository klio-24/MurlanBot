import secrets
import boto3
import json
import random
import copy

from MonteCarloTreeSearch import mcts
from MurlanState import game_state
from GameParams import standard_deck
from GameParams import MCTSMeta

class Game:
    def __init__(self):
        self.history = []
        self.session_id = secrets.token_hex(16)

        # Initialize DynamoDB client and table only once
        self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
        self.table = self.dynamodb.Table('game_sessions')

    def play_move(self, move):
        response = f"You chose: {self.load_from_db()}"
        self.history.append(response)
        return "\n".join(self.history)
    
    def save_game_state_to_db(self,new_state):
        self.table.put_item(Item={"session_id": self.session_id}) # ADD TO THIS THE GAME STATE

    def load_game_state_from_db(self):
        response = self.table.get_item(Key={"session_id": self.session_id})
        return response.get('Item') # MODIFY TO RETURN THE GAME STATE


    def to_dict(self):
        return {
            'on_table': copy.deepcopy(self.on_table),
            'bot_hand': copy.deepcopy(self.bot_hand),
            'player_hand': copy.deepcopy(self.player_hand),
            'bot_possible_cards': copy.deepcopy(self.bot_possible_cards)
        }
    def from_dict(self, data):
        state = cls()
        state.on_table = copy.deepcopy(data.get('on_table', []))
        state.bot_hand = copy.deepcopy(data.get('bot_hand', []))
        state.player_hand = copy.deepcopy(data.get('player_hand', []))
        state.bot_possible_cards = copy.deepcopy(data.get('bot_possible_cards', []))
        return state
    
    # def process_move(input,hand):
    #     numbers = [int(x)-1 for x in input.split('/') if x.isdigit()] # does the processing (minus one as indexes on screen start from 1)

    #     translated_hand = []

    #     for i in numbers:
    #         translated_hand.append(hand[i]) # converts processed indexes to the play

    #     return translated_hand

    # need to change this where it just accepts a game state and plays one round of the game

    def initialise_game(self):
        deck = standard_deck.deck.copy() 

        random.shuffle(deck)

        player_hand = []
        bot_hand = []
        cards = 13

        for i in range(cards):
            player_hand.append(deck.pop())
            bot_hand.append(deck.pop())

        # Ensuring the shuffled hands are in the same order as the deck so the lookups work right
        deck_order = {id(card): idx for idx, card in enumerate(standard_deck.deck)}
        player_hand = sorted(player_hand, key=lambda card: deck_order[id(card)])
        bot_hand = sorted(bot_hand, key=lambda card: deck_order[id(card)])

        # Initialise game state with initial conditions
        state = game_state()
        state.on_table = []
        state.bot_hand = bot_hand
        state.player_hand = player_hand
        state.bot_possible_cards = deck

        # Save the initial game state to the database
        self.save_game_state_to_db()

    def process_player_move(self, player_move, player_hand, state):
        processed_hand = player_hand[player_move-1]
        state.move(processed_hand, "player")
        # Store the updated game state in the database
        self.save_game_state_to_db()
        return True

    def play_a_turn(self,stored_game_state,player_move):

        MCTS = mcts(stored_game_state)
        stored_game_state
        
        # before processing the move, we check if bot has any valid moves
        # if len(stored_game_state.valid_moves(stored_game_state.bot_hand,stored_game_state.on_table)) == 0:
            # store the updated game state in the database
            
            # return information that bot skips turn

    
        MCTS.search(MCTSMeta.SEARCH_TIME) # performs the search algorithm to find the best move

        num_rollouts, run_time = MCTS.stats()

        bot_move = MCTS.best_move() 
        stored_game_state.move(bot_move,"bot")

        # removed the need to move the root of the MCTS as generating a new tree each move
        
      
        game_status = stored_game_state.game_status() # checks the game status
        return game_status, bot_move, num_rollouts, run_time
    
