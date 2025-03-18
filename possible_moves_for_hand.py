def possible_moves_for_hand(hand):

# test = player1_hand[0]["rank"]

    moves = []



    # single  
    for card in hand:
        moves.append(["single", 1, [card]]) # this is the default 'play hand', so the structure is a list of the hand kind (single, double, straight), then the hand size, then the actual hand
        

    # double

    

    # triple

    # quad

    # for card in hand:
    #     if rank is equal to the next three cards in the hand:
    #         moves.append([card, next card, next next card, next next next card])

    # straight

    # for card in hand:
        
    #     if hand(card+1).rank

    #     if rank of first card is equal to the rank of the next card minus 1 and this applies for at least 5 cards:
    #         if it doesnt contain rank of black joker or rank of black jocker

    #             if it doesnt contain  K  and ace and two
    #         (make sure this means 5 cards and 6 cards and 7 cards work etc etc)
    

    # # prison straight

    # for card in hand:
    #     if rank of first card is equal to the rank of the next card minus 1 and theres 3 of those, then one minus for the next
    #         if it doesnt contain rank of black joker or rank of black jocker

    #             if it doesnt contain  K  and ace and two
    


    return moves

