#!/usr/bin/env python3

from wordle import Player, GameManager
from scipy.stats import entropy
from wordlist import *
from information import *
from wordle import *
import copy

class Solver(Player):
    """
    "Solving" Wordle

    Your task is to fill in this class to automatically play the game.
    Feel free to modify any of the starter code.

    You Should write at least three subclasses of Player.
    1. A Random Player -- guess a random word each time!
    2. A Player that uses Matt Parker's 5 Words. 
       2a. How do you leveage the info gained from these 5 words?
       2b. Do always you have to guess all of these words?
       3b. What order should you guess these words in?
    3. Entropy Player (You are welcome to use the scipy above)
    4. Better and Better Players!

    Your goal is not just to Write the BEST SOLVER YOU CAN, but scientifically
    show that your solver is better than the others. 

    Note that the GameManager class returns the number of guesses a player makes.
    Compute 3 statistics:
    (1) the average number of guesses
    (2) the max number of guesses
    (3) the minimum number of guesses

    Think deeply about how you should design this experiments. How should you select the
    experimental inputs? Is it better for the two algorithms youre comparing to have the
    same or different test sets between experiments?
    
    Please use objects and inheritance to structure your experiments.

    Here's an outline of the rest of the code in this project.
    - wordle.py.
      Hit play when VSCode is focused on this file to play
      a game of wordle against the computer! There are 3 classes
      of interest to the Solver:
      +  `Wordle` manages the world game state itself
      +  `Player` Provides a Human interface at the CLI to play the game
          Your Solver exposes the same interface as this class       
      +  `Game Manager` runs the main control loop for Wordle

    - information.py
      This file defines how information is propagated to the player. The relevant
      classes are `Information` and `Pattern`.
      + Pattern records a list `pattern` that represents the outcomes. 
        For instance
            [hit, miss, miss, mem, hit]
        Means the first and last letters of a guess are correct, the second two
        are not in the word, and the penultimate is in the word but not
        in the right spot. These codes are defined in `Code`.

      + Pattern provides a useful method `pattern.matches(guess, word)` which
        checks that the current pattern is consistent with guessing `guess` when
        `word` is the goal word

      + Information is constructed by passing it a player-provided `guess` and
        the `goal` word. 
        
      + Information provides an important method `info.matches(word)` which 
        returns true if `info.pattern == Information(info.guess, word)`

      + IMPORTANT. The `patterns()` function returns a list of all 3^5 patterns.

    - `wordlist.py`
       This file defines the `WordList` class, which is not actually a `list`,
       but wraps a list, defining some helpful wordle-specific features.
       + wordlist.get_random_word() gets a random word from the wordlist
       + wordlist.refine(info) keeps only those words consistent with `info`
       + wordlist.matching(pattern, guess) produces a literal `list`
         of words that such that if they had been the goal word, would have 
         produced pattern in responds to a player guessing `guess.
    """
    def __init__(self, method = "custom"): #method takes in "random", "matt", "entropy"
      self.num_guesses = 0
      self.wordlist = WordList()
      self.method = method

    def update_knowledge(self, info):
      """
      update_knowledge updates the solver's knowledge with an `info`
      info is an element of the `Information` class. See `information.py`
      """
      self.wordlist.refine(info)
      print(info)

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
            total_patterns = patterns()
            entropy_word_pair = [0, ""] # [Entropy, entropy word]
            for word in self.wordlist:
                pattern_distribution = [len(self.wordlist.matching(pattern, word))/len(self.wordlist) for pattern in total_patterns]
                e = entropy(pattern_distribution)
                if e >= entropy_word_pair[0]:
                    entropy_word_pair = [e, word]
            return entropy_word_pair[1]

        # Draft of pseudo-code for applying entropy algorithm twice (entropy for every possible two guesses)
        else: 
            """
            1. make copy of wordlist, call it wordlist_copy
            2. loop through wordlist with a nested for-loop
            3. set max_combined_entropy = 0
            4. find max_entropy, max_entropy_word, probability_distribution like normal
            5. for each possible pattern, refine wordlist_copy and find the second_max_entropy and second_max_entropy_word
            6. weight each second_max_entropy with corresponding pattern_probability and aggregate sum
            7. add this aggregate sum to first max_entropy, update max_combined_entropy if greater
            8. return """        
            return ""

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
    entr = Benchmark(solver, 100, "entropy")
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
