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
class Output:
    """
    The Output class is responsible for displaying all output to the user.
    """

    def show_banner(self):
        """Shows a pre-defined banner on the output stream."""
        self.show_content("#" * 50)

    def show_line(self, modifier):
        """
        Shows a line

        Parameters:
            modifier (String): a value that is prepended to the line.
        """
        if modifier is None:
            modifier = ""
        self.show_content(modifier + ("-" * 30))

    def show_content(self, content):
        """
        Shows content on the output stream.

        Parameters:
            content (string): The content to be displayed.
        """
        print(content)

    def show_strategy_menu(self):
        """Prints the game strategy selection menu"""
        self.show_content("Please select a strategy for your opponent "
                          "from the numbered list.")
        self.show_content("\t1 - The Rock: always plays 'rock'")
        self.show_content("\t2 - You'll never guess!")
        self.show_content("\t3 - Monkey see, monkey do: "
                          "repeats every move you play!")
        self.show_content("\t4 - The Cylist: cycles through "
                          "the moves in ordered manner.")
        self.show_line(None)


class Player:

   
    def move(self):
      
        return 'rock'

    def learn(self, my_move, their_move):
     
        pass

    def name(self):
        return "Computer"




class RandomPlayer(Player):
 
    def move(self):
         return random.choice(moves)

class HumanPlayer(Player):
 
    def move(self):
       
        while True:
            my_move = input("Rock, paper, scissors? > ").lower().strip()
            if self.is_valid_move(my_move):
                break
        return my_move

    def is_valid_move(self, my_move):
       
        return my_move in moves

    def name(self):
        return "Player"


class ReflectPlayer(Player):
   

    def __init__(self):
        
        self.my_move = random.choice(moves)

    def move(self):
         return self.my_move

    def learn(self, my_move, their_move):
        
        self.my_move = their_move



class CyclePlayer(Player):
   

    def __init__(self):
       
        self.move_index = 0

    def move(self):
         return moves[self.move_index]

    def learn(self, my_move, their_move):
       
        self.move_index = 0 if self.move_index == 2 else self.move_index + 1



def beats(one, two):
   
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
   

    def __init__(self, p1, p2, output):
        
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.rounds_to_play = 0
        self.rounds_played = 0
        self.output = output
        self.number_ties = 0

    def show_welcome(self):
         self.output.show_content("\n")
        self.output.show_banner()
        self.output.show_content("Welcome to Rock, Paper, Scissors!")
        self.output.show_banner()
        self.output.show_content("\n")

    def ask_strategy(self):
       
        self.output.show_strategy_menu()
        while True:
            strategy = input("Select a strategy 1-4: ")
            if(strategy.isdigit()):
                strategy = int(strategy)
                if strategy == 1:
                    return Player()
                elif strategy == 2:
                    return RandomPlayer()
                elif strategy == 3:
                    return ReflectPlayer()
                elif strategy == 4:
                    return CyclePlayer()

    def randomize_first_player(self):
         rnd = random.randint(1, 10)
        if rnd >= 5:
            # Switch p1 and p2
            self.p1 = type(self.p2)()
            self.p2 = HumanPlayer()

    def ask_number_rounds(self):
        
        while True:
            rounds = input("How many rounds would you like to "
                           " play [0-10]? ".strip())
            if(rounds.isdigit()):
                rounds = int(rounds)
                if rounds >= 0 and rounds <= 10:
                    return int(rounds)

    def score_round(self, p1_move, p2_move):
        
        if beats(p1_move, p2_move):
            self.p1_score += 1
            return f"** {self.p1.name().upper()} WINS! **"
        elif beats(p2_move, p1_move):
            self.p2_score += 1
            return f"** {self.p2.name().upper()} WINS! **"
        else:
            self.number_ties += 1
            return "** TIE GAME! **"

    def show_game_outcome(self, winner):
       
        self.output.show_content("\n")
        self.output.show_banner()
        if winner is None:
            self.output.show_content("Game Over")
        else:
            self.output.show_content(f"Game Over: {winner} wins the game!")
        self.output.show_content("Final scores:")
        self.output.show_content(f"\t{self.p1.name()}: ".ljust(15) +
                                 f"{self.p1_score} rounds")
        self.output.show_content(f"\t{self.p2.name()}: ".ljust(15) +
                                 f"{self.p2_score} rounds")
        self.output.show_content(f"\tTies: ".ljust(15) +
                                 f"{self.number_ties} rounds")
        self.output.show_line("\t")
        self.output.show_content("\tTotal rounds: ".ljust(15) +
                                 f"{self.rounds_played}")
        self.output.show_banner()

    def show_score(self):
        """Shows the current score of each player."""
        self.output.show_content(f"Score: {self.p1.name()}: "
                                 f"{self.p1_score}, "
                                 f"{self.p2.name()}: {self.p2_score}")

    def play_round(self):
        """Plays a round of the game and shows the outcome."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.output.show_content(f"{self.p1.name()}: {move1}  "
                                 f"{self.p2.name()}: {move2}")

        self.output.show_content(self.score_round(move1, move2))
        self.show_score()

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def determine_game_winner(self):
        
        if self.p1_score > self.p2_score:
            return self.p1.name()
        elif self.p2_score > self.p1_score:
            return self.p2.name()

    def play_game(self):
       
        self.show_welcome()
        self.p2 = self.ask_strategy()
        self.randomize_first_player()
        self.rounds_to_play = self.ask_number_rounds()
        self.output.show_content("Go!")
        winner = None
        while self.rounds_played < self.rounds_to_play:
            self.rounds_played += 1
            self.output.show_content(f"\nRound {self.rounds_played}:")
            self.play_round()

        winner = self.determine_game_winner()
        self.show_game_outcome(winner)


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player(), Output())
    game.play_game()





