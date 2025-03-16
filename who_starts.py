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