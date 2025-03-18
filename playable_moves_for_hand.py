def playable_moves_for_hand(current_play,hand,free_turn):
    
    moves = []
    for card in hand:
        if free_turn:
            moves.append(card)
        else:
            if current_play["rank"] < card["rank"]:
                moves.append(card)
        
    
    
    return moves