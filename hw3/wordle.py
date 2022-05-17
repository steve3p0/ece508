""" ECE 508 Spring 2022
    Dr. Schubert
    Steve Braich sbraich@pdx.edu
    PSU ID: 953378420

    Your solutions should include the code to solve each problem and a transcript (e.g. screenshots) of your
    programs working. The assessment of your code will consider comment quality, clarity/readability,
    maintainability, algorithm and code efficiency.

    2) Wordle: Write a function to play the game of Wordle. The object of the game is to identify a secret
       five letter word by receiving clues based on your guesses. After each guess, your function should
       provide a five-character string that indicates whether each character guess is correct or not.
          a. If a guess character is correct, output a *
          b. If the guess character is in the word, but not in the correct position, output a +
          c. Otherwise, output a

       For testing use the following list of possible words. Next week's lecture will discuss how a much
       lengthier list might instead be read from a file.

       words = ["apple", "about", "carrot", "zebra", "table", "scarf", "dozen"]

       Here's a couple example runs:

       --------------------------------------------------------------------------------------
       |>>> wordle()                                                                        |
       |...                                                                                 |
       |    Guess: apple                                                                    |
       |    1: apple +..**                                                                  |
       |    Guess: zatle                                                                    |
       |    2: zatle .*+**                                                                  |
       |    Guess: tamle                                                                    |
       |    3: tamle **.**                                                                  |
       |    Guess: table                                                                    |
       |    YES!                                                                            |
       --------------------------------------------------------------------------------------

       The default number of guesses a player can make should be 5, but your function should optionally
       accept a max number of guesses. Also, your function should do some amount of error checking

       --------------------------------------------------------------------------------------
       |>>> wordle(3)                                                                       |
       |...                                                                                 |
       |    Guess: airplane                                                                 |
       |    need a 5 letter guess                                                           |
       |    Guess: airpl                                                                    |
       |    1: airpl +.+..                                                                  |
       |    Guess: chart                                                                    |
       |    2: chart ..+*.                                                                  |
       |    Guess: foody                                                                    |
       |    3: foody .....                                                                  |
       |    Sorry, too many guesses                                                         |
       --------------------------------------------------------------------------------------

"""

import random

# create a word list that the random index can pull from
words = ["apple", "about", "carrot", "zebra", "table", "scarf", "dozen"]
# set the word length
WORD_LENGTH = 5


def wordle(attempts: int = 5, word_index: int = random.randint(0, len(words))) -> str:
    """  Write a function to play the game of Wordle. T
    :param attempts: The number of allowed attempts
    :type attempts: int (default 5)
    :param word_index: The index of the correct word (used for testing)
    :type word_index: int (default random)
    :return: output to the user
    :rtype: str
    """

    # loop for the number of attempts
    for i in range(attempts):
        valid_guess = False
        # make sure the guess is valid
        while valid_guess is False:
            guess = input(f"Guess: ")
            if len(guess) != WORD_LENGTH:
                print(f"need a 5 letter guess")
            else:
                valid_guess = True

        # start building the output string
        output = f"{i + 1}: {guess} "

        if guess == words[word_index]:
            print(f"YES!")
            exit()
        else:
            for g, c in zip(guess, words[word_index]):
                if g == c:
                    output += "*"
                elif g in words[word_index]:
                    output += "+"
                else:
                    output += "."
        print(output)

    print(f"Sorry, too many guesses")


if __name__ == '__main__':

    # Test first example in assignment description
    wordle(word_inex=4)

    # Test second example in assignment description
    wordle(attempts=3, word_index=3)

