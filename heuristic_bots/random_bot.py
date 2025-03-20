# bot that selects a random move in the set of possible moves
from random import random
def random_bot(playable_moves):
    return random.choice(playable_moves)