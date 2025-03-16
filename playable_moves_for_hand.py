def playable_moves_for_hand(current_card,hand,free_turn):
    
    moves = []
    for card in hand:
        if free_turn:
            moves.append(card)
        else:
            if current_card["rank"] < card["rank"]:
                moves.append(card)
        
    
    return moves