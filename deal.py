import random

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
