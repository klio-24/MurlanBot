import secrets
import boto3
import random

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
        self.save_game_state_to_db(state)

    
    def save_game_state_to_db(self, new_state):
        item = {    
            "session_id": self.session_id,
            "game_state": new_state.to_dict()  # serialize the game state
        }
        self.table.put_item(Item=item)

    def load_game_state_from_db(self):
        response = self.table.get_item(Key={"session_id": self.session_id})
        item = response.get('Item')
        if not item or 'game_state' not in item:
            return None  # Or raise an error / start new game
        return game_state.from_dict(item['game_state'])  # deserialize the game state
    
    # def process_move(input,hand):
    #     numbers = [int(x)-1 for x in input.split('/') if x.isdigit()] # does the processing (minus one as indexes on screen start from 1)
    #     translated_hand = []
    #     for i in numbers:
    #         translated_hand.append(hand[i]) # converts processed indexes to the play
    #     return translated_hand

    def play_move(self, player_move):

        state = self.load_game_state_from_db()


        processed_hand = [state.player_hand[int(player_move)-1]]
        state.move(processed_hand, "player")

        self.save_game_state_to_db(state)


    def bot_play_a_turn(self):

        stored_game_state = self.load_game_state_from_db()  # Load the game state from the database

        MCTS = mcts(stored_game_state)
        

        
        # before processing the move, we check if bot has any valid moves
        # if len(stored_game_state.valid_moves(stored_game_state.bot_hand,stored_game_state.on_table)) == 0:
            # store the updated game state in the database
            
            # return information that bot skips turn

    
        MCTS.search(MCTSMeta.SEARCH_TIME) # performs the search algorithm to find the best move

        num_rollouts, run_time = MCTS.stats()

        bot_move = MCTS.best_move() 
        stored_game_state.move(bot_move,"bot")

        # removed the need to move the root of the MCTS as generating a new tree each move
        
        self.save_game_state_to_db(stored_game_state)  # Save the updated game state to the database


    
    def game_status(self):
        status = self.load_game_state_from_db()
        player_hand = status.player_hand
        bot_hand = status.bot_hand

        if len(player_hand) == 0:
            return 1
        elif len(bot_hand) == 0:
            return 2
        else:
            return 0

    def get_state_text(self, cur_state):
        output = []



        if len(cur_state.bot_hand) > 1:
            output.append("Opponent has many cards left")
        else:
            output.append("Opponent has 1 card left")

        if cur_state.on_table:
            output.append("Move on table is:")
            for card in cur_state.on_table:
                output.append(f"{card['card']} of {card['suit']}")
        else:
            output.append("You have a free turn")

        output.append("Your Hand:")
        for i, card in enumerate(cur_state.player_hand):
            output.append(f"{i+1}: {card['card']} of {card['suit']}")

        output.append("Opponent's Hand:")
        for i, card in enumerate(cur_state.bot_hand):
            output.append(f"{i+1}: {card['card']} of {card['suit']}")

        return "\n".join(output)
    
