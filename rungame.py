from deck import deck
from deal import deal
from print_hand_nicely import print_hand_nicely
from possible_moves_for_hand import possible_moves_for_hand
from print_moves_nicely import print_moves_nicely
from playable_moves_for_hand import playable_moves_for_hand
from who_starts import who_starts
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

while len(player1_hand) !=0 or len(player2_hand) != 0:
    
    print_hand_nicely(player1_hand)
    print("Type 0 to pass")
    ind = int(input())
    current_card = player1_hand[ind-1]

    if ind == 0:
        print("You passed")
        free_turn = True
        cards = playable_moves_for_hand(current_card, player2_hand, free_turn)
    if ind != 0:
        player1_hand.remove(current_card)
        free_turn = False
        print("You played:", current_card["card"],"of" ,current_card["suit"])
        cards = playable_moves_for_hand(current_card, player2_hand, free_turn)

    if len(cards) == 0:
        print("Computer passed")
    else:
        card = cards[0]
        print("Computer played:", card["card"],"of" ,card["suit"])
        player2_hand.remove(card)

    if len(player1_hand) == 0:
        print("---You won---")
        break
    if len(player2_hand) == 0:
        print("---Computer won---")
        break

    
# show results



# run game 2
round = 2

    # deal the cards



    # do handicap

    # run the game

# show results

