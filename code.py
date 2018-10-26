#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


"""
index = randm.randint(0,2)
return moves[index]
"""


class Player:

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass
    def name(self):
        return "Computer"

class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))
