import random
from MCTS import mcts
from MurlanState import game_state
from GameParams import standard_deck


def play():
    deck = standard_deck()

    random.shuffle(deck)

    player_hand = []
    bot_hand = []
    cards = 13

    for i in range(cards):
        player_hand.append(deck.pop())
        bot_hand.append(deck.pop())

    game_state()

    game_state.on_table = []
    game_state.bot_hand = bot_hand
    game_state.player_hand = player_hand
    game_state.bot_possible_cards = deck

    while not game_state.game_over():
        game_state.print_state()
        
        user_move = input("To skip, type '0', or select moves by picking the cards based on the number before the semicolon, in ascending order, and seperated by a '/': ")

        while processed_move not in game_state.get_legal_moves():

            if int(user_move) == 0:
                game_state.move(0,"player")
            
            else:
                processed_move = []
                temp = []
                for i in user_move:
                    if not i.isnumeric() or i == "/":
                        print("not valid move")
                game_state.make_move(processed_move,"player")

            if game_state.game_over():
                "Game over: You win!"

            bot_hand = mcts.make_move
            print("The bot played:")
            break
        
        if game_state.game_over():
            "Game over: Bot won!"

if __name__ == "__main__": # this line ensures game is played only when this script is run and not and import of this script in another file
    play()