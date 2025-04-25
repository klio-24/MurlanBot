# defines game class

class game_state:
    def __init__(self):
        self.on_table = []
        self.legal = []
        self.free_turn = None
        self.bot_hand = []
        self.player_hand = [] 


    def valid_moves(self,hand,free_turn):

                playable_moves = []
        if free_turn == 1:
        
        # is there a way to index the full possible moves so they are ordered in groups
        if current_play[0] == "single":
            for i in possible_moves:
                if i[2]["rank"] > current_play[2]["rank"]:
                    playable_moves.append(i[2])
        
        elif current_play[0] == "double":


        elif current_play[0] == "triple":

        else:
            
        if free_turn:
            for i in hand:
                self.legal.append(i)
        else:
            for i in hand and not free_turn:
                if i > self.on_table:
                    self.legal.append(i)

    def game_over(self):
        if len(opp_hand) == 0:
            return -1
        if len(ai_hand) == 0:
            return 1
        return 0
    
    def print_state(self):
        if not free_turn:
        print("Move on table is:")

        if len(bot_hand)>1:
            print("Opponent has many cards left")
        else:
            print("Opponent has 1 card left")
    
        print("Your Hand")


        for ind,card in enumerate(hand):
            print(ind+1,": ", card["card"], " of ", card["suit"], sep='')
         