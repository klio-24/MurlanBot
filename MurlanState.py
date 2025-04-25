# defines game class

class game_state:
    def __init__(self):
        self.on_table = []
        self.bot_hand = []
        self.player_hand = [] 


    def valid_moves(self,hand,free_turn):
        res = []
        if free_turn:
            for i in self.player_hand:
                res.append(i)
        else:
            return res
             

    def game_over(self):
        if len(self.player_hand) == 0:
            return -1
        if len(self.bot_hand) == 0:
            return 1
        return 0
    
    def print_state(self):
        if self.on_table:
            print("Move on table is:")
            for ind,card in enumerate(self.on_table):
                print(card["card"], " of ", card["suit"], sep='')
        else:
            print("You have a free turn")

        if len(self.bot_hand)>1:
            print("Opponent has many cards left")
        else:
            print("Opponent has 1 card left")
    
        print("Your Hand:")
        for ind,card in enumerate(self.player_hand):
            print(ind+1,": ", card["card"], " of ", card["suit"], sep='')
         