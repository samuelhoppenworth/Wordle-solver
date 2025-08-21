#!/usr/bin/env python3

from wordle import Player, GameManager
from scipy.stats import entropy
from wordlist import *
from information import *
from wordle import *
import copy

class Solver(Player):
    def __init__(self, method): # method: "random", "matt" or "entropy"
      self.num_guesses = 0
      self.wordlist = WordList()
      self.method = method

    def update_knowledge(self, info):
      """
      update_knowledge updates the solver's knowledge with an `info`
      info is an element of the `Information` class. See `information.py`
      """
      self.wordlist.refine(info)
      # print(info)

    def find_entropy_value(self, wordlist):
        total_patterns = patterns()
        entropy_word_pair = [0, ""] # [Entropy, word]

        for word in wordlist:
            pattern_distribution = [len(wordlist.matching(pattern, word))/len(wordlist) for pattern in total_patterns]
            e = entropy(pattern_distribution)
            if e >= entropy_word_pair[0]:
                entropy_word_pair = [e, word]
        return entropy_word_pair


    def make_guess(self):
        # Random function
        if self.method == "random": 
          guess = self.wordlist.get_random_word()
          return guess
        
        # Matt Parker function
        elif self.method == "matt":
            while self.num_guesses < 5:
                matt = ["fjord", "gucks", "nymph", "vibex", "waltz"]
                guess = matt[self.num_guesses]
                self.num_guesses += 1
                return guess
            return self.wordlist.get_random_word()
        
        # Entropy function
        elif self.method ==  "entropy":
            entropy_word_pair = self.find_entropy_value(self.wordlist) 
            return entropy_word_pair[1]

class Benchmark():
    def __init__(self, player, iterations, method):
        self.player = player
        self.guess_sum = 0
        self.iterations = iterations
        self.method = method
        self.max = 0
        self.min = float("inf")

    def game_simulate(self):
        num_guess = 0
        start_wordlist = copy.deepcopy(self.player.wordlist)
        for _ in range(self.iterations):
            self.player.wordlist = copy.deepcopy(start_wordlist)
            g = GameManager(self.player, self.method)
            num_guess = g.play_game()
            self.guess_sum += num_guess
            if num_guess > self.max:
                self.max = num_guess
            if num_guess < self.min:
                self.min = num_guess
        return
    
    def average_num_guesses(self):
        return self.guess_sum/self.iterations
    def max_guesses(self):
        return self.max
    
    def min_guesses(self):
        return self.min
    
    
def main():    
    solver = Solver("random")
    ran = Benchmark(solver, 1000, "random")
    ran.game_simulate()

    solver = Solver("matt")
    matt = Benchmark(solver, 1000, "matt")
    matt.game_simulate()

    solver = Solver("entropy")
    entr = Benchmark(solver, 1000, "entropy")
    entr.game_simulate()
    
    print("Random Generator Testing")
    print(f"Average guess amount: {ran.average_num_guesses()}")
    print(f"Minimum guesses: {ran.min_guesses()}")
    print(f"Maximum guesses: {ran.max_guesses()}\n")


    print("Matt Parker Testing")
    print(f"Average guess amount: {matt.average_num_guesses()}")
    print(f"Minimum guesses: {matt.min_guesses()}")
    print(f"Maximum guesses: {matt.max_guesses()}\n")

    print("Entropy Testing")
    print(f"Average guess amount: {entr.average_num_guesses()}")
    print(f"Minimum guesses: {entr.min_guesses()}")
    print(f"Maximum guesses: {entr.max_guesses()}\n")


if __name__ == "__main__": main()

