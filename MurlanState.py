# defines game class

from collections import Counter
from itertools import combinations
import random

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

            # # Doubles 
            # rank_counts = Counter(card["rank"] for card in hand)
            # for rank, count in rank_counts.items():
            #     if count >= 2:
            #         cards_of_rank = [card for card in hand if card["rank"] == rank]
            #         for combo in combinations(cards_of_rank, 2):
            #             res.append(list(combo))

            # # Triple
            # for rank, count in rank_counts.items():
            #     if count >= 3:
            #         cards_of_rank = [card for card in hand if card["rank"] == rank]
            #         for combo in combinations(cards_of_rank, 3):
            #             res.append(list(combo))

        else:
            power_to_beat = on_table[0]["rank"]
            if len(hand) == 1:
                # Single
                for card in hand:
                    if card["rank"] > power_to_beat:
                        res.append([card])

            # elif len(hand) == 2:
            #     # Double
            #     rank_counts = Counter(card["rank"] for card in hand)
            #     for rank, count in rank_counts.items():
            #         if count >= 2 and rank > power_to_beat:
            #             cards_of_rank = [card for card in hand if card["rank"] == rank]
            #             for combo in combinations(cards_of_rank, 2):
            #                 res.append(list(combo))

            # else:
            #     # Triple
            #     rank_counts = Counter(card["rank"] for card in hand)
            #     for rank, count in rank_counts.items():
            #         if count >= 3 and rank > power_to_beat:
            #             cards_of_rank = [card for card in hand if card["rank"] == rank]
            #             for combo in combinations(cards_of_rank, 3):
            #                 res.append(list(combo))
        return res

    def game_over(self):
        if len(self.player_hand) == 0 or len(self.bot_hand) == 0:
            return True 
    
    def get_result(self):
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
        
    def print_state(self):

        if len(self.bot_hand)>1:
            print("Opponent has many cards left")
        else:
            print("Opponent has 1 card left")
    
        if self.on_table:
            print("Move on table is:")
            for ind,card in enumerate(self.on_table):
                print(card["card"], " of ", card["suit"], sep='')
        else:
            print("You have a free turn")

        print("Your Hand:")
        for ind,card in enumerate(self.player_hand):
            print(ind+1,": ", card["card"], " of ", card["suit"], sep='')
         