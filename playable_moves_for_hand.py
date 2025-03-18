def playable_moves_for_hand(current_play,possible_moves,free_turn):
    
    playable_moves = []
    if free_turn == 1:
        return possible_moves
    
    # is there a way to index the full possible moves so they are ordered in groups
    if current_play[0] == "single":
        for i in possible_moves:
            if i[2]["rank"] > current_play[2]["rank"]:
                playable_moves.append(i[2])
    
    elif current_play[0] == "double":


    elif current_play[0] == "triple":

    
    elif current_play[0] == "quad":


    elif current_play[0] == "straight":

    
    

    
    
    
    