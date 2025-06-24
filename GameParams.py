# Defines game parameters, MCTS parameters, and deck (technically a game parameter as you could play with different decks)
import math

class standard_deck:

    three_spades = {
    "card": "three",
    "suit": "spades",
    "rank": 0
    }

    four_spades = {
        "card": "four",
        "suit": "spades",
        "rank": 1
    }

    five_spades = {
        "card": "five",
        "suit": "spades",
        "rank": 2
    }

    six_spades = {
        "card": "six",
        "suit": "spades",
        "rank": 3
    }

    seven_spades = {
        "card": "seven",
        "suit": "spades",
        "rank": 4
    }

    eight_spades = {
        "card": "eight",
        "suit": "spades",
        "rank": 5
    }

    nine_spades = {
        "card": "nine",
        "suit": "spades",
        "rank": 6
    }

    ten_spades = {
        "card": "ten",
        "suit": "spades",
        "rank": 7
    }

    jack_spades = {
        "card": "jack",
        "suit": "spades",
        "rank": 8
    }

    queen_spades = {
        "card": "queen",
        "suit": "spades",
        "rank": 9
    }

    king_spades = {
        "card": "king",
        "suit": "spades",
        "rank": 10
    }

    ace_spades = {
        "card": "ace",
        "suit": "spades",
        "rank": 11
    }

    two_spades = {
        "card": "two",
        "suit": "spades",
        "rank": 12
    }

    three_hearts = {
        "card": "three",
        "suit": "hearts",
        "rank": 0
    }

    four_hearts = {
        "card": "four",
        "suit": "hearts",
        "rank": 1
    }

    five_hearts = {
        "card": "five",
        "suit": "hearts",
        "rank": 2
    }

    six_hearts = {
        "card": "six",
        "suit": "hearts",
        "rank": 3
    }

    seven_hearts = {
        "card": "seven",
        "suit": "hearts",
        "rank": 4
    }

    eight_hearts = {
        "card": "eight",
        "suit": "hearts",
        "rank": 5
    }

    nine_hearts = {
        "card": "nine",
        "suit": "hearts",
        "rank": 6
    }

    ten_hearts = {
        "card": "ten",
        "suit": "hearts",
        "rank": 7
    }

    jack_hearts = {
        "card": "jack",
        "suit": "hearts",
        "rank": 8
    }

    queen_hearts = {
        "card": "queen",
        "suit": "hearts",
        "rank": 9
    }

    king_hearts = {
        "card": "king",
        "suit": "hearts",
        "rank": 10
    }

    ace_hearts = {
        "card": "ace",
        "suit": "hearts",
        "rank": 11
    }

    two_hearts = {
        "card": "two",
        "suit": "hearts",
        "rank": 12
    }

    three_diamonds = {
        "card": "three",
        "suit": "diamonds",
        "rank": 0
    }

    four_diamonds = {
        "card": "four",
        "suit": "diamonds",
        "rank": 1
    }

    five_diamonds = {
        "card": "five",
        "suit": "diamonds",
        "rank": 2
    }

    six_diamonds = {
        "card": "six",
        "suit": "diamonds",
        "rank": 3
    }

    seven_diamonds = {
        "card": "seven",
        "suit": "diamonds",
        "rank": 4
    }

    eight_diamonds = {
        "card": "eight",
        "suit": "diamonds",
        "rank": 5
    }

    nine_diamonds = {
        "card": "nine",
        "suit": "diamonds",
        "rank": 6
    }

    ten_diamonds = {
        "card": "ten",
        "suit": "diamonds",
        "rank": 7
    }

    jack_diamonds = {
        "card": "jack",
        "suit": "diamonds",
        "rank": 8
    }

    queen_diamonds = {
        "card": "queen",
        "suit": "diamonds",
        "rank": 9
    }

    king_diamonds = {
        "card": "king",
        "suit": "diamonds",
        "rank": 10
    }

    ace_diamonds = {
        "card": "ace",
        "suit": "diamonds",
        "rank": 11
    }

    two_diamonds = {
        "card": "two",
        "suit": "diamonds",
        "rank": 12
    }

    three_clubs = {
        "card": "three",
        "suit": "clubs",
        "rank": 0
    }

    four_clubs = {
        "card": "four",
        "suit": "clubs",
        "rank": 1
    }

    five_clubs = {
        "card": "five",
        "suit": "clubs",
        "rank": 2
    }

    six_clubs = {
        "card": "six",
        "suit": "clubs",
        "rank": 3
    }

    seven_clubs = {
        "card": "seven",
        "suit": "clubs",
        "rank": 4
    }

    eight_clubs = {
        "card": "eight",
        "suit": "clubs",
        "rank": 5
    }

    nine_clubs = {
        "card": "nine",
        "suit": "clubs",
        "rank": 6
    }

    ten_clubs = {
        "card": "ten",
        "suit": "clubs",
        "rank": 7
    }

    jack_clubs = {
        "card": "jack",
        "suit": "clubs",
        "rank": 8
    }

    queen_clubs = {
        "card": "queen",
        "suit": "clubs",
        "rank": 9
    }

    king_clubs = {
        "card": "king",
        "suit": "clubs",
        "rank": 10
    }

    ace_clubs = {
        "card": "ace",
        "suit": "clubs",
        "rank": 11
    }
    
    two_clubs = {
        "card": "two",
        "suit": "clubs",
        "rank": 12
    }

    # joker_black = {
    #     "card": "black joker",
    #     "suit": "",
    #     "rank": 13
    # }

    # joker_red = {
    #     "card": "red joker",
    #     "suit": "",
    #     "rank": 14
    # }

    deck = [
        three_spades, three_hearts, three_diamonds, three_clubs,
        four_spades, four_hearts, four_diamonds, four_clubs,
        five_spades, five_hearts, five_diamonds, five_clubs,
        six_spades, six_hearts, six_diamonds, six_clubs,
        seven_spades, seven_hearts, seven_diamonds, seven_clubs,
        eight_spades, eight_hearts, eight_diamonds, eight_clubs,
        nine_spades, nine_hearts, nine_diamonds, nine_clubs,
        ten_spades, ten_hearts, ten_diamonds, ten_clubs,
        jack_spades, jack_hearts, jack_diamonds, jack_clubs,
        queen_spades, queen_hearts, queen_diamonds, queen_clubs,
        king_spades, king_hearts, king_diamonds, king_clubs,
        ace_spades, ace_hearts, ace_diamonds, ace_clubs,
        two_spades, two_hearts, two_diamonds, two_clubs
    ]

    # deck = [
    #     three_spades, three_hearts, three_diamonds, three_clubs,
    #     four_spades, four_hearts, four_diamonds, four_clubs,
    #     five_spades, five_hearts, five_diamonds, five_clubs,
    #     six_spades, six_hearts, six_diamonds, six_clubs,
    #     seven_spades, seven_hearts, seven_diamonds, seven_clubs,
    #     eight_spades, eight_hearts, eight_diamonds, eight_clubs,
    #     nine_spades, nine_hearts, nine_diamonds, nine_clubs,
    #     ten_spades, ten_hearts, ten_diamonds, ten_clubs,
    #     jack_spades, jack_hearts, jack_diamonds, jack_clubs,
    #     queen_spades, queen_hearts, queen_diamonds, queen_clubs,
    #     king_spades, king_hearts, king_diamonds, king_clubs,
    #     ace_spades, ace_hearts, ace_diamonds, ace_clubs,
    #     two_spades, two_hearts, two_diamonds, two_clubs,
    #     joker_black, joker_red
    # ]

class GameMeta:
    deck = standard_deck.deck

class MCTSMeta:
    EXPLORATION = 3 # UNDERSTAND THIS VALUE LATER
    SEARCH_TIME = 3 # seconds

