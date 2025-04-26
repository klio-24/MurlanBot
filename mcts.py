# Monte Carlo Tree Search Agent
from MurlanState import game_state
import time
import random

# each tree node needs two values: probability of the AI winning from that node; amount of times node visited

class Node:
    def __init__(self,move,parent):
        self.move = move
        self.parent = parent
        self.N = 0 # number of sims from this node
        self.Q = 0 # win rate at this node
        self.children = {}
        self.turn = 0 # I think this should be like 0: player turn, 1: Bot turn
        self.result = 0 # I think this should be like 0: continue, 1: Bot wins, 2: player wins
    
    
class mcts:
    def __init__(self, state = game_state()):
        self.root = Node(None,None)
    



        res = []

        random.shuffle(deck)

        return deck[0:opponent_hand_size-1]

    def select_node(self):
        for i in Node.children:
            # select the smallest N

    def expand(self):
        if game_state.game_over():
            return False

        if bot_turn:
            children = [Node(simulated_bot_hand,parent) for move in game_state.get_legal_moves()]
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
