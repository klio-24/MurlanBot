def print_moves_nicely(hand):
    for set in hand:
        
        lenset = len(set)
        for card in set:
            print(card["card"], "of", card["suit"])

            if lenset > 1:
                print ("+")
                lenset = lenset - 1
        print()
    