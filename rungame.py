from deck import deck
from deal import deal
from print_hand_nicely import print_hand_nicely
from possible_moves_for_hand import possible_moves_for_hand
from print_moves_nicely import print_moves_nicely
from playable_moves_for_hand import playable_moves_for_hand
from helper_functions.who_starts import who_starts
import random


round = 1

# deal the cards
[player1_hand,player2_hand] = deal(round, deck)

# sort the hands

player1_hand.sort(key=lambda x: x['rank'])
player2_hand.sort(key=lambda x: x['rank'])
# run game 1


start = who_starts(player1_hand,player2_hand)
print("Player", start, "starts")

possible_moves = possible_moves_for_hand(player1_hand)

# show results



# run game 2
round = 2

    # deal the cards



    # do handicap

    # run the game

# show results

