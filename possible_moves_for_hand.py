
from collections import defaultdict
from itertools import combinations

def possible_moves_for_hand(hand):

# test = player1_hand[0]["rank"]

    moves = []



    # single  
    for card in hand:
        moves.append(["single", 1, [card]]) # this is the default 'play hand', so the structure is a list of the hand kind (single, double, straight), then the hand size, then the actual hand
        

    # double

    # triple

    # Dictionary to count occurrences of each rank
    rank_count = defaultdict(list)
    
    # Group cards by their rank (storing full card information)
    for card in hand:
        rank = card[:-1]  # Extract the rank (remove the suit)
        rank_count[rank].append(card)
    
    # List to store all possible triplet combinations
    triplet_combinations = []
    
    # For each rank, generate combinations of 3 cards if there are 3 or more cards
    for rank, cards in rank_count.items():
        if len(cards) >= 3:
            # Generate all combinations of 3 cards from the list of cards
            triplet_combinations.extend(combinations(cards, 3))
    
    return moves