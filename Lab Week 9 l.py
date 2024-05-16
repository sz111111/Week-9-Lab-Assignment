# -*- coding: utf-8 -*-
"""
Created on Thu May 16 00:34:33 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)



import random

class RockPaperScissors:
    def __init__(self, num_players):
        self.choices = ['rock', 'paper', 'scissors']
        self.num_players = num_players
        self.results = {'wins': 0, 'losses': 0, 'ties': 0}
    
    def get_human_choice(self):
        choice = input('Pick one of rock, paper or scissors: ')
        while choice not in self.choices:
            print("Invalid choice. Please choose again.")
            choice = input('Pick one of rock, paper or scissors: ')
        return choice
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, p1, p2):
        if p1 == p2:
            print(f"Both players selected {p1}. It's a tie!")
            self.results['ties'] += 1
        elif (p1 == 'rock' and p2 == 'scissors') or \
             (p1 == 'scissors' and p2 == 'paper') or \
             (p1 == 'paper' and p2 == 'rock'):
            print(f"{p1} beats {p2}! You win!")
            self.results['wins'] += 1
        else:
            print(f"{p2} beats {p1}. You lose!")
            self.results['losses'] += 1
    
    def play_game(self):
        if self.num_players == 0:
            p1 = self.get_computer_choice()
            p2 = self.get_computer_choice()
        elif self.num_players == 1:
            p1 = self.get_human_choice()
            p2 = self.get_computer_choice()
        else:
            p1 = self.get_human_choice()
            p2 = self.get_human_choice()

        self.determine_winner(p1, p2)
        print(f"Current Score: Wins: {self.results['wins']}, Losses: {self.results['losses']}, Ties: {self.results['ties']}")

    def start_game(self):
        rounds = int(input("How many rounds would you like to play? "))
        for _ in range(rounds):
            self.play_game()
        print("Final Score:", self.results)

# Example usage
num_players = int(input("How many human players? (0-2): "))
game = RockPaperScissors(num_players)
game.start_game()
