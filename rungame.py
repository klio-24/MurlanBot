from print_hand_nicely import print_hand_nicely
from playable_moves_for_hand import playable_moves_for_hand
from who_starts import who_starts
import random


    

    
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
def deal(round, deck):

    random.shuffle(deck)

    player1_hand = []
    player2_hand = []
    
    if round == 1:
        cards = 13
    if round == 2:
        cards = 14

    for i in range(cards):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())

    return player1_hand, player2_hand


round = 1

# deal the cards
[player1_hand,player2_hand] = deal(round, deck)

# sort the hands

player1_hand.sort(key=lambda x: x['rank'])
player2_hand.sort(key=lambda x: x['rank'])
# run game 1


start = who_starts(player1_hand,player2_hand)
print("Player", start, "starts")
# show results

def play():
    
    while not state.game_over():
        state.print()
    
        user_move = input("To skip, type '0', or select moves by picking the cards based on the number before the semicolon, in ascending order, and seperated by a '/': ")

        while processed_move not in state.get_legal_moves():

        if int(user_move) == 0:
            state.move(0)
        
        else:
            processed_move = []
            temp = []
            for i in user_move:
                if not i.isnumeric() or i == "/":

            state.make_move(processed_move)

        if state.game_over():
            "Game over: You win!"

        bot_hand = mcts.make_move
        print("The bot played:")
        break
        print_moves_nicely(bot_hand)
        
        if state.game_over():
            "Game over: Bot won!"




if __name__ == "__main__": # this line ensures game is played only when this script is run and not and import of this script in another file
    play()