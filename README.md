# n-coin-circle-game
Implementation of a coin game with the following rules: 

There are n coins (numbered 1 through n, clockwise) in a circle, each showing either heads or tails. Starting from coin 1, 
and proceeding clockwise one coin at a time, players are allowed to flip the current coin using the following rules: if the 
current coin is showing heads, then Player 1 can choose to flip it to tails or to pass; if the current coin is showing tails, 
then Player 2 can choose to flip that coin to heads or to pass. In either case, play then immediately proceeds to the next coin, 
and can loop around the circle as many times as needed. Player 1 wins if all n coins ever end up facing the same way (all heads or 
all tails).

## Running the game
This game can be played by the downloading the repo and executing the command "python3 game.py" on the command line. You must use 
Python 3.4 or later.

## Game strategy
See STRATEGY.md

