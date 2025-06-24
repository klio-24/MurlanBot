# defines game class

import copy
import random

from collections import Counter
from itertools import combinations
class game_state:
    def __init__(self):
        self.on_table = []
        self.bot_hand = []
        self.player_hand = [] 
        self.bot_possible_cards = []
        self.turn = 0 # 0 is player turn, 1 is bot turn

    def get_result(self):
        if len(self.player_hand) == 0:
            return 1
        elif len(self.bot_hand) == 0:
            return 2
        else:
            return 0
        
    def game_over(self):
        if len(self.player_hand) == 0 or len(self.bot_hand) == 0:
            return True 
    
        
    def valid_moves(self,hand,on_table):
        res = []

        if on_table:
            res.append([])  # Empty move is valid if cards are on the table - you can't skip your turn

        if not on_table:
            # Single 
            for card in hand:
                res.append([card])

        else:
            power_to_beat = on_table[0]["rank"]
        # Single
            for card in hand:
                if card["rank"] > power_to_beat:
                    res.append([card])

        # FIX THIS CONDITION (WHY ARE THEY len(hand) == 2)
        #     # Double
        #     rank_counts = Counter(card["rank"] for card in hand)
        #     for rank, count in rank_counts.items():
        #         if count >= 2 and rank > power_to_beat:
        #             cards_of_rank = [card for card in hand if card["rank"] == rank]
        #             for combo in combinations(cards_of_rank, 2):
        #                 res.append(list(combo))

        return res

    

        
    def move(self, move, player):
        if player == "player":
            if move:
                for card in move:
                    self.player_hand.remove(card)
                self.on_table = move
            else:
                # Player skips
                self.on_table = []
        elif player == "bot":
            if move:
                for card in move:
                    self.bot_hand.remove(card)
                self.on_table = move
            else:
                # Bot skips
                self.on_table = []

        self.turn = 1 - self.turn
        
    def random_possible_bot_hand(self,turn,bot_hand,player_hand_size):
        if turn == "bot":
            for i in range(player_hand_size):
                self.bot_possible_cards.pop(self.bot_possible_cards.index(i))
        else:
            for i in bot_hand:
                self.bot_possible_cards.pop(self.bot_possible_cards.index(i))

        random.shuffle(self.bot_possible_cards)

        return self.bot_possible_cards[0:player_hand_size-1]
        

    def to_dict(self):
        return {
            'on_table': copy.deepcopy(self.on_table),
            'bot_hand': copy.deepcopy(self.bot_hand),
            'player_hand': copy.deepcopy(self.player_hand),
            'bot_possible_cards': copy.deepcopy(self.bot_possible_cards),
            'turn': self.turn  
        }

    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.on_table = copy.deepcopy(data.get('on_table', []))
        state.bot_hand = copy.deepcopy(data.get('bot_hand', []))
        state.player_hand = copy.deepcopy(data.get('player_hand', []))
        state.bot_possible_cards = copy.deepcopy(data.get('bot_possible_cards', []))
        state.turn = data.get('turn', 0)  
        return state
         