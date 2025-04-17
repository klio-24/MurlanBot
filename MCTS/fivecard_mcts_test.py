import time
import random
import math

opp_hand = [3,5,7,9,11]
ai_hand = [4,6,8,10,12]

# each tree node needs two values: probability of the AI winning from that node; amount of times node visited

class game_state:
    def __init__(self):
        self.last_played = []
        self.on_table = None
        self.legal = []

    def get_legal_moves(self,hand):
        for i in hand:
            if i > self.on_table:
                self.legal.append(i)

    def check_win(self):
        if len(opp_hand) == 0:
            return -1
        if len(ai_hand) == 0:
            return 1
        return 0


class Node:
    def __init__(self,move,parent):
        self.move = move
        self.parent = parent
        self.N = 0 # number of sims from this node
        self.Q = 0 # win rate at this node
        self.children = {}
    



class MCTS:
    def __init__(self):
        self.root = Node(None,None)
    

    def select_node(self):
        for i in Node.children:
            # select the smallest N

    def expand(self):
        if game_state.game_over():
            return False

        children = [Node(move,parent) for move in game_state.get_legal_moves()]

    def rollout(self, game_state):
        while not game_state.game_over():
            random.choice(game_state.get_legal_moves(ai_hand))


    def backpropogate(self):

    def select_move(self):
        # after time up, select move with highest Q through sorting

        # move root
    def run(self, time_limit):
        start_time = time.process_time()

        rollout_count = 0
        while time.process_time - start_time <= time_limit:
            # run MCTS

            rollout_count += 1




def run_game(): 





run_game()