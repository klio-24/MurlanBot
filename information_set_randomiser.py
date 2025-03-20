# this script generates a random set of states for the AI model for cards opponent has in their hands (Information Set Monte Carlo Tree Search approach), using cards already played to make the random output more accurate
import random
def information_set_randomiser(played_cards,deck,hand,opponent_hand_size):

    for i in played_cards:

        if i in deck:
            deck.pop(deck.index(i))

    for i in hand:
        if i in deck:
            deck.pop(deck.index(i))

    res = []

    random.shuffle(deck)

    return deck[0:opponent_hand_size-1]