# Monte Carlo Tree Search Agent

import time
import random
import math

from copy import deepcopy
from GameParams import MCTSMeta
from MurlanState import game_state

# each tree node needs two values: probability of the AI winning from that node; amount of times node visited

class Node:
    def __init__(self,move,parent):
        self.move = move
        self.parent = parent
        self.N = 0 # number of sims from this node
        self.Q = 0 # win rate at this node
        self.children = {}
        self.result = 0 # I think this should be like 0: continue, 1: Bot wins, 2: player wins
    def value(self):
        if self.N == 0:
            return float('inf')
        return self.Q / self.N + MCTSMeta.EXPLORATION * math.sqrt(math.log(self.parent.N) / self.N)      
      
    
class mcts:
    def __init__(self, state = game_state()):
        self.root_state = deepcopy(state)
        self.root = Node(None,None)
        self.run_time = 0
        self.node_count = 0
        self.num_rollouts = 0
        self.search_time = MCTSMeta.SEARCH_TIME
    
    def select_node(self,node): # algorithm to select node, picks all with maximum value for searching, then randomly selects one of them
        
        node = self.root
        state = deepcopy(self.root_state)

        while node.children: 
            children = list(node.children.values())
            random.shuffle(children) # avoids bias by selecting random best child
            node = max(children, key=lambda child: child.value())

        
        return node
        

    def expand(self, parent: Node, state: game_state): # for a selected node, it gives it all children nodes which are possible
        
        if state.game_over():
            return False

        for move in state.valid_moves():
            parent.children[move] = Node(move, parent)
        return True

    def rollout(self, state = game_state): # performs random moves on this node until the end and gets the outcome

        while not state.game_over():
            move = random.choice(state.valid_moves())
            state.move(move)
        return state.get_result()  
    
    def backpropogate(self, node): # traverses back up the tree while updating values along the way
        while node is not None:  
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

    def search(self): # performs the actual MCTS
        start_time = time.process_time()
        t_max = self.search_time
        num_rollouts = 0
        while time.process_time() - start_time < t_max:
            node, state = self.select_move()
            self.backpropogate(node, self.rollout(state))
            num_rollouts += 1
        run_time = time.process_time() - start_time
        self.run_time = run_time
        self.num_rollouts = num_rollouts

    def move(self, move): # moves the root of the tree to the new state
        if move in self.root.children:
            self.root_state.move(move) # need to move our copy of the state aswell to ensure both are in sync
            self.root = self.root.children[move]
            return
        
        self.root_state.move(move)
        self.root = Node(None)
      
    def best_move(self): # returns the best move from the root node
        if self.root_state.game_over():
            return [-1]

        if move in self.root.children:
            self.root = self.root.children[move]
        
        mcts.search(self.search_time)
        move = mcts.best_move()
        best_child = max(self.root.children.values(), key=lambda n: n.N/n.Q if n.N > 0 else -1)  
        self.root = self.root.children[move]

        return best_child.move

    def stats(self):
        return self.num_rollouts, self.run_time
