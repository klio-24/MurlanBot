# MurlanBot


## System Diagram

![Diagram](diagram.jpg)

## Initial MCTS Development and Refactoring 



## Conclusion
This project utilises Monte Carlo Tree Search https://en.wikipedia.org/wiki/Monte_Carlo_tree_search (MCTS) to create a bot capable of playing shedding-style card games https://en.wikipedia.org/wiki/List_of_shedding-type_games.

In these types of games, it is not always optimal to play the lowest card possible at each turn. For example, if Player 1 has a 3 and a 6, and Player 2 has a 4 and a 7, if P2 played 4 instead of 7 if P1 plays 3, P2 would lose.

MCTS works by exploring possible moves at each turn and then selecting the move with the highest probability of winning. The MCTS code was developed using the following tutorial: https://www.harrycodes.com/blog/monte-carlo-tree-search

The program is deployed on a website using AWS Lambda to run a Flask app packaged using Zappa, with other AWS services used to facilitate the API calls and custom domain, namely API Gateway and Route 53.

The game can be played at https://murlanbot.xyz

