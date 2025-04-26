import random
from MCTS import mcts
from MurlanState import game_state
from GameParams import standard_deck

def process_move(input,hand):
    numbers = [int(x)-1 for x in input.split('/') if x.isdigit()]

    translated_hand = []

    for i in numbers:
        translated_hand.append(hand[numbers])

    return translated_hand

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

        if len(game_state.valid_moves()) == 0:
            print("You have no valid moves, it's the Bot's turn again!")
            continue

        else:
            while process_move(user_move,game_state.player_hand) not in game_state.valid_moves():
                user_move = input("To skip, type '0', or select moves by picking the cards based on the number before the semicolon, in ascending order, and seperated by a '/': ")
            
            if game_state.game_over():
                print("Game over: You win!")

            bot_hand = mcts.make_move()
            print("The bot played:")

            
            if game_state.game_over():
                "Game over: Bot won!"

if __name__ == "__main__": # this line ensures game is played only when this script is run and not and import of this script in another file
    play()