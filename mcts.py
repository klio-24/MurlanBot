# Monte Carlo Tree Search Agent
from MurlanState import game_state
import time
import random
from copy import deepcopy

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
        self.root_state = deepcopy(state)
        self.root = Node(None,None)
        self.run_time = 0
        self.node_count = 0
        self.num_rollouts = 0
    
    def select_node(self): # algorithm to select node, picks all with maximum value for searching, then randomly selects one of them
        while len(node.children) != 0:
            children = node.children.values()
            max_val = max(children, key=lambda n: n.value())

    def expand(self, parent: Node, state: game_state): # for a selected node, it gives it all children nodes which are possible
        if game_state.game_over():
            return False

        if bot_turn:
            children = [Node(simulated_bot_hand,parent) for move in game_state.get_legal_moves()]
        children = [Node(move,parent) for move in game_state.get_legal_moves()]

    def rollout(self, game_state): # performs random moves on this node until the end and gets the outcome
        while not game_state.game_over():
            random.choice(game_state.get_legal_moves(ai_hand))

    def backpropogate(self): # traverses back up the tree while updating values along the way
        while not node:  
            if self.result == 1 and self.turn == 1: # Bot won and currently on a bot node
                node.Q += 1
            elif self.result == 2 and self.turn == 0: # Player won and currently on a player node
                node.Q += 1
            elif self.result == 1 and self.turn == 0: # Bot won and currently a player node
                node.Q += 0
            elif self.result == 2 and self.turn == 1: # Player won and currently a bot node
                node.Q += 0
            node.N += 1
            node = node.parent

    def search(self, t_max: int): # performs the actual MCTS

    def select_move(self): # after time up, select move with highest Q through sorting
        
    def move_root(self,move): # moves root of tree based on result
    
    def stats(self):
        return self.num_rollouts, self.run_time
