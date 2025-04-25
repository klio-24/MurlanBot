import random
from MCTS import mcts
from MurlanState import game_state
from GameParams import standard_deck


def play():
    
    deck = standard_deck()
    player_biggest_spade = 100
    bot_biggest_spade = 100

    for cards in player1_hand:
        if cards["suit"] == "spades":
            player_biggest_spade = cards["rank"]
            break

    for cards in player2_hand:
        if cards["suit"] == "spades":
            bot_biggest_spade = cards["rank"]
            break
    
    if player_biggest_spade < bot_biggest_spade:
        player_start = True
    else:
        player_start = False


    random.shuffle(deck)

    player1_hand = []
    player2_hand = []
    cards = 13

    for i in range(cards):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())


    while not game_state.game_over():
        game_state.print()
    
        user_move = input("To skip, type '0', or select moves by picking the cards based on the number before the semicolon, in ascending order, and seperated by a '/': ")

        while processed_move not in game_state.get_legal_moves():

            if int(user_move) == 0:
                game_state.move(0)
            
            else:
                processed_move = []
                temp = []
                for i in user_move:
                    if not i.isnumeric() or i == "/":
                        print("not valid move")
                game_state.make_move(processed_move)

            if game_state.game_over():
                "Game over: You win!"

            bot_hand = mcts.make_move
            print("The bot played:")
            break
        
        if game_state.game_over():
            "Game over: Bot won!"

if __name__ == "__main__": # this line ensures game is played only when this script is run and not and import of this script in another file
    play()