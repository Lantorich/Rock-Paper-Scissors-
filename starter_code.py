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


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))


class HumanPlayer(Player):
    def move(self):
        answer = input("""Choose your move - Rock, Paper or """
                       """Scissors? To exit press x\n""")
        while answer not in moves and answer != 'x':
            answer = input("Enter a valid move!")
        return answer


class ReflectPlayer(Player):
    pass


class CyclePlayer(Player):
    pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, RandomPlayer, HumanPlayer):
        self.RandomPlayer = RandomPlayer()
        self.HumanPlayer = HumanPlayer()
        self.count_wins = 0
        self.count_losses = 0
        self.count_ties = 0
        self.score1 = 0
        self.score2 = 0
        move1 = self.RandomPlayer.move()
        move2 = self.HumanPlayer.move()

    def score(self):
        if beats(move1, move2):
            self.count_wins += 1
            print (self.count_wins)
        if HumanPlayer.move == RandomPlayer.move:
            self.count_ties += 1
        elif beats(move2, move1):
            self.count_losses += 1

    def play_round(self):
        #  print(self.count_wins)
        move1 = self.RandomPlayer.move()
        move2 = self.HumanPlayer.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        self.score1 = self.count_wins
        self.score2 = self.count_wins
        print(f"Player 1 Score: {self.score1} /
              Player 2 Score: {self.score2}")

        self.RandomPlayer.learn(move1, move2)
        self.HumanPlayer.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(6):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()




