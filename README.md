**Wordle Solver**

Completed July, 2023

At Jane Street's Academy of Math and Programming, I implemented three algorithms that solve the New York Times's Wordle. The first algorithm randomly selects a word from a word bank, shrinks the word bank in 
accordance with the information gained from making the guess (i.e., if you guess "ADIEU" and the program tells you "E" is not the target word, then all words with "E" are removed from the word bank), and repeats. 

The second algorithm's first 5 guesses are "fjord", "gucks", "nymph", "vibex", and "waltz", which span 25 of the 26 letters of the alphabet, then make guesses using the first algorithm's logic. The motivation 
behind this approach is that by guessing these words, you have information on almost all of the letters of the alphabet. Credit goes to YouTuber Matt Parker for discovering this combination of words. 

The third algorithm uses the concept of Shannon entropy to determine the guess that would yield the most information gain. The algorithm iterates through every possible word and calculates the "pattern distribution"
for that word. A "pattern" in this context is the color output of the program on a given guess, i.e., the pattern for the target word is GREEN GREEN GREEN GREEN GREEN, as all are guessed in the correct order. 
The pattern distribution, then, is the probability distribution of the patterns that a word can illicit. The program then calculates the Shannon entropy (the measure of uncertainty or information content) of each 
pattern distribution and returns the word with the highest entropy.

After writing robust automated unit tests for these algorithms, I was able to compare their efficiencies. The best one, expectedly, was the shannon entropy function, which correctly guessed the target word 
in an average of 3.51 guesses.

**Takeaways**

From this project, I learned about the concept of Shannon entropy and its implications in information theory. I also gained experience writing automated test cases and comparing algorithm efficiency.
