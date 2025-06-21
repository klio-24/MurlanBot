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

    
    def game_status(self):
        if len(self.player_hand) == 0:
            return 1
        elif len(self.bot_hand) == 0:
            return 2
        else:
            return 0
        
    def move(self,cards,player):
        for i in cards:
            if player == "bot":
                self.bot_hand.remove(i)
            elif player == "player":
                self.player_hand.remove(i)
        self.on_table = cards
        self.turn = 1 if player == "player" else 0 # here is where we switch turn value

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
            'bot_possible_cards': copy.deepcopy(self.bot_possible_cards)
        }
    
    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.on_table = copy.deepcopy(data.get('on_table', []))
        state.bot_hand = copy.deepcopy(data.get('bot_hand', []))
        state.player_hand = copy.deepcopy(data.get('player_hand', []))
        state.bot_possible_cards = copy.deepcopy(data.get('bot_possible_cards', []))
        return state
    
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
         