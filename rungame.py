import random
from MonteCarloTreeSearch import mcts
from MurlanState import game_state
from GameParams import standard_deck

def process_move(input,hand):
    numbers = [int(x)-1 for x in input.split('/') if x.isdigit()] # does the processing (minus one as indexes on screen start from 1)

    translated_hand = []

    for i in numbers:
        translated_hand.append(hand[numbers]) # converts processed indexes to the play

    return translated_hand

def play():
    deck = standard_deck.deck.copy() 

    random.shuffle(deck)

    player_hand = []
    bot_hand = []
    cards = 13

    for i in range(cards):
        player_hand.append(deck.pop())
        bot_hand.append(deck.pop())

    # Ensuring the shuffled hands are in the same order as the deck so the lookups work right
    deck_order = {id(card): idx for idx, card in enumerate(standard_deck.deck)}
    player_hand = sorted(player_hand, key=lambda card: deck_order[id(card)])
    bot_hand = sorted(player_hand, key=lambda card: deck_order[id(card)])


    # Initialise game state with initial conditions
    state = game_state()
    state.on_table = []
    state.bot_hand = bot_hand
    state.player_hand = player_hand
    state.bot_possible_cards = deck

    MCTS = mcts(state)

    while not state.game_over():
        state.print_state()

        if len(state.valid_moves(state.player_hand,state.on_table)) == 0:
            print("You have no valid moves, it's the Bot's turn again!")
            continue

        else:
            user_move = input("Select moves by picking the cards based on the number before the semicolon, in ascending order, and separated by a '/': ")
            while user_move not in state.valid_moves(state.player_hand,state.on_table):
                print("Invalid move. Try again.")
                user_move = input("Select moves by picking the cards based on the number before the semicolon, in ascending order, and separated by a '/': ")
            
            state.move(user_move,"player")
            MCTS.move(user_move) # moves the root of the tree to the new state
            print("You played:")
            for ind,card in enumerate(user_move):
                print(ind+1,": ", card["card"], " of ", card["suit"], sep='')
            if state.game_over():
                print("Game over: You win!")
                break
            
        if len(state.valid_moves(state.bot_hand,state.on_table)) == 0:
            print("Bot has no valid moves, it's your turn again!")
            continue
        else:
            bot_move = MCTS.make_move()
            num_rollouts, run_time = MCTS.stats()
            state.move(bot_move,"bot")
            MCTS.move(bot_move)

            print("Search algorithm performed ", num_rollouts, "rollouts in ", run_time, "seconds")

            print("The bot played:")
            for ind,card in enumerate(bot_move):
                print(ind+1,": ", card["card"], " of ", card["suit"], sep='')
            
            if state.game_over():
                "Game over: Bot won!"
                break

if __name__ == "__main__": # this line ensures game is played only when this script is run and not and import of this script in another file
    play()