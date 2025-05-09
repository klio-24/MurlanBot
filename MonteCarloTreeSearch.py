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
    
    def select_node(self): # algorithm to select node, picks all with maximum value for searching, then randomly selects one of them
        
        node = self.root
        state = deepcopy(self.root_state)

        while node.children: 
            children = list(node.children.values())
            random.shuffle(children) # avoids bias by selecting random best child
            node = max(children, key=lambda child: child.value())
            state.move(node.move)

        
        return node, state
        

    def move_to_tuple(self,move): # converts the move to a tuple so it can be used as a key in the dictionary
        return tuple(sorted((card["card"], card["suit"], card["rank"]) for card in move))
    def tuple_to_move(self, move_tuple):
        return [{"card": card, "suit": suit, "rank": rank} for (card, suit, rank) in move_tuple]

    def expand(self, parent: Node, state: game_state): # for a selected node, it gives it all children nodes which are possible
        
        if state.game_over():
            return False

        for move in state.valid_moves():
            parent.children[self.move_to_tuple(move)] = Node(move, parent)
        return True

    def rollout(self): # performs random moves on this node until the end and gets the outcome
        state = deepcopy(self.root_state) # we don't keep the nodes along the way, just want the outcome
        current_turn = state.turn
        # rollout needs to track current turn so backpropogate then knows whos turn it is, and therefore what value to assign
        while not state.game_over():
            if state.turn == 0: # player turn
                move = random.choice(state.valid_moves(state.player_hand,state.on_table))
            else: # bot turn
                move = random.choice(state.valid_moves(state.bot_hand,state.on_table))
            state.move(move,"bot" if state.turn == 1 else "player")
        result = state.get_result()
        return result, current_turn
    
    def backpropogate(self, node, result, turn): # traverses back up the tree while updating values along the way
        # we need to pass in result and turn so we know what to update: you can't use self result and self turn because they are not set yet
        while node is not None:
            if result == 1 and turn == 1:
                node.Q += 1
            elif result == 2 and turn == 0:
                node.Q += 1
            node.N += 1
            node = node.parent

    def search(self,t_max): # performs the actual MCTS
        start_time = time.process_time()
        num_rollouts = 0
        while time.process_time() - start_time < t_max:
            node, state = self.select_node()
            result, turn = self.rollout()

            self.backpropogate(node, result, turn)
            num_rollouts += 1
        run_time = time.process_time() - start_time
        self.run_time = run_time
        self.num_rollouts = num_rollouts


    def best_move(self): # returns the best move from the root node
        if self.root_state.game_over():
            return [-1]

        
        # we need to find all those moves with the highest value, then randomly select one of them so as not to bias the search to one branch

        max_value = max(self.root.children.values(), key=lambda n: n.N).N
        max_nodes = [n for n in self.root.children.values() if n.N == max_value]
        best_child = random.choice(max_nodes)

        return best_child.move
    
    def move(self, move,player): # moves the root of the tree to the new state
        
        if self.move_to_tuple(move) in self.root.children:
            self.root_state.move(move) # need to move our copy of the state aswell to ensure both are in sync
            self.root = self.root.children[self.move_to_tuple(move)]
            return
        
        self.root_state.move(move,player)
        self.root = Node(None,None)
      


    def stats(self):
        return self.num_rollouts, self.run_time
