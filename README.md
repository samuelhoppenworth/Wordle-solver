# Wordle Solver

Completed July, 2023

### Naive algorithm

The first algorithm randomly selects a word from a word bank, shrinks the word bank in accordance with the information gained from making the guess (i.e., if you guess "ADIEU" and the program tells you "E" is not the target word, then all words with "E" are removed from the word bank), and repeats. 

### Matt Parker algorithm

The second algorithm guesses the same five words every time: *fjord, gucks, nymph, vibex,* and *waltz*. When guessed together, these words provide information on 25 of the 26 letters of the alphabet. From there, the Naive algorithm is applied to the now greatly diminished bank of possible words. YouTuber and mathematician Matt Parker discovered this combinations of words in his video [Can you find: five five-letter words with twenty-five unique letters?](https://www.youtube.com/watch?v=_-AfhLQfb6w)

### Entropy-Based Algorithm

The third algorithm uses Shannon entropy to predict which guess provides the most information gain. Shannon entropy measures the level of uncertainty within a probability distribution. In other words, a distribution with higher entropy indicates a more uniform spread of probabilities across its possible outcomes, while a distribution with lower entropy is more concentrated or predictable.

For example, consider rolling a fair 100-sided die versus a fair 6-sided die. The probability distribution of the 100-sided die has higher entropy because its outcomes are spread across 100 equally likely possibilities, whereas the 6-sided die has only 6. As a result, there is significantly more uncertainty about the outcome of the 100-sided die compared to the 6-sided die.

In Wordle, this concept is applied by analyzing the possible color patterns that can result from guessing a particular word. A color pattern represents the feedback provided by the game, such as GREEN GREEN GREEN GREEN GREEN for a correct guess. Each word generates a distribution of possible color patterns, where each pattern has a probability based on how often it occurs relative to the target word.

So, a word with higher entropy produces color patterns that are more evenly distributed, indicating greater uncertainty in the outcomes. This higher uncertainty translates to more information gained on average, as such a guess effectively narrows down the possible target words more efficiently than a word with a more predictable or concentrated pattern distribution.

#### Algorithm pseudo-code

1. Pattern Distribution:
   - For each word in the word list, calculate all possible color patterns that could result from guessing that word
   - Each pattern corresponds to a subset of the word list that matches that pattern
   - The probability of each pattern is the size of that subset divided by the total number of words in the list

2. Entropy Calculation:
   - Compute the entropy of the pattern distribution using the formula: E = -Σ p_i log₂(p_i)
     where \( p_i \) is the probability of the \( i \)-th pattern
   - Higher entropy indicates a more uniform distribution of patterns, meaning the guess is more informative

3. Selecting the Best Guess:
   - Iterate through all possible words in the word list, compute the entropy for each, and select the word with the highest entropy
   - This word is the one that, on average, provides the most information about the target word, helping to eliminate the largest number of possibilities in this step


### Results

By creating an automated test suite, I was able to compare efficiencies of these algorithms. The best one, expectedly, was the shannon entropy algorithm, which correctly guessed the target word 
in an average of 3.51 guesses.
