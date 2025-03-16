def print_hand_nicely(hand):

    ind = 1
    for card in hand:
        print(ind,": ", card["card"], " of ", card["suit"], sep='') 
        ind = ind + 1
    
