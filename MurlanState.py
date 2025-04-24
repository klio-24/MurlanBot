# defines game class




class game_state:
    def __init__(self):
        self.last_played = []
        self.on_table = None
        self.legal = []

    def get_legal_moves(self,hand,free_turn):

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

    def check_win(self):
        if len(opp_hand) == 0:
            return -1
        if len(ai_hand) == 0:
            return 1
        return 0