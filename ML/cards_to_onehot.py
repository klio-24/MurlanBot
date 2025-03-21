def cards_to_onehot(hand,opponent_hand,table,deck):

    onehot_hand = [0] * 54
    onehot_opp = [0] * 54
    onehot_table = [0] * 54

    for i in hand:
        onehot_hand[deck.index(i)]
    for i in opponent_hand:
        onehot_opp[deck.index(i)]
    for i in table:
        onehot_table[deck.index(i)]

    res = [onehot_hand,onehot_opp,onehot_table]

    return res

