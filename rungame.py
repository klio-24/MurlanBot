from print_hand_nicely import print_hand_nicely
from playable_moves_for_hand import playable_moves_for_hand
from who_starts import who_starts
import random

def print_hand_nicely(hand):

    ind = 1
    for card in hand:
        print(ind,": ", card["card"], " of ", card["suit"], sep='') 
        ind = ind + 1
    

    
def who_starts(player1_hand,player2_hand):

    player1_power = None
    player2_power = None

    for cards in player1_hand:
        if cards["suit"] == "spades":
            player1_power = cards["rank"]
            break

    for cards in player2_hand:
        if cards["suit"] == "spades":
            player2_power = cards["rank"]
            break
    
    if player1_power > player2_power:
        val = 1
    else:
        val = 2

    return val
def deal(round, deck):

    random.shuffle(deck)

    player1_hand = []
    player2_hand = []
    
    if round == 1:
        cards = 13
    if round == 2:
        cards = 14

    for i in range(cards):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())

    return player1_hand, player2_hand


round = 1

# deal the cards
[player1_hand,player2_hand] = deal(round, deck)

# sort the hands

player1_hand.sort(key=lambda x: x['rank'])
player2_hand.sort(key=lambda x: x['rank'])
# run game 1


start = who_starts(player1_hand,player2_hand)
print("Player", start, "starts")
# show results

def play():

    print:
        Opponent has x cards remaining
    
        "Your Cards:"
    

if __name__ == "__main__": # this line ensures game is played only when this script is run and not and import of this script in another file
    play()