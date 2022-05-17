""" ECE 508 Spring 2022
    Dr. Schubert
    Steve Braich sbraich@pdx.edu
    PSU ID: 953378420

    Your solutions should include the code to solve each problem and a transcript (e.g. screenshots) of your
    programs working. The assessment of your code will consider comment quality, clarity/readability,
    maintainability, algorithm and code efficiency.

    1) Most Frequent Word: Write a function that asks repeatedly asks a user for lines of text input until
       the user enters a blank line. The function mfw() should print out the most frequently used word in
       the lines of text. Use a dictionary in your solution. Below is an example test case. Note that Idle
       chooses to display Python keywords in orange.

       --------------------------------------------------------------------------------------
       |>>> mfw()                                                                           |
       |    this is some text that is using                                                 |
       |... the word is a lot of times.                                                     |
       |... What is the word most frequently used?                                          |
       |                                                                                    |
       |    Most Frequent Word: is (used 4 times)                                           |
       |>>> mfw()                                                                           |
       |    apples and banannas                                                             |
       |    banannas and apples                                                             |
       |                                                                                    |
       |    Most Frequent Word: apples (used 2 times)                                       |
       |    Most Frequent Word: and (used 2 times)                                          |
       |    Most Frequent Word: bananas (used 2 times)                                      |
       --------------------------------------------------------------------------------------

"""


def mfw() -> str:
    """ Find the most frequent word by repeatedly taking in input lines of text until the user enters a blank line
    :return: The most frequent word and the frequency of the word
    :rtype:
    """

    # create word dictionary
    words = {}

    # loop thru user input until empy line
    while True:
        line = input("")
        if len(line.strip()) == 0:
            break

        # split the line into words
        for w in line.split(' '):
            if w in words:
                words[w] += 1
            # initialize new entry
            else:
                words[w] = 1

    # Get the max word frequency
    max_freq = max(list(words.values()))

    # Get max word
    for w, count in words.items():
        if count == max_freq:
            print(f"Most Frequent Word: {w} (used {max_freq} times)")


if __name__ == '__main__':

    mfw()
