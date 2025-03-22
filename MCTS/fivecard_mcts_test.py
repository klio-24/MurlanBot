opp_hand = [3,5,7,9,11]
ai_hand = [4,6,8,10,12]

# each tree node needs two values: probability of the AI winning from that node; amount of times node visited

class MurlanState:
    def __init__(self):
        self.last_played = []

    def get_legal_moves(self):
    
    def check_win(self):


class Node:
    def __init__(self,move,parent):
        self.move = move
        self.parent = parent
        self.N = 0 # number of sims from this node
        self.Q = 0 # win rate at this node
        self.children = {}
    



class MCTS:
    def __init__(self):
    

    def select_node(self):

    def expand(self):

    def rollout(self):


    def backpropogate(self):

