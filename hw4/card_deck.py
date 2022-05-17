""" ECE 508 Spring 2022
    Dr. Schubert
    Steve Braich sbraich@pdx.edu
    PSU ID: 953378420

    Your solutions should include the code to solve each problem and a transcript (e.g. screenshots) of your
    programs working. The assessment of your code will consider comment quality, clarity/readability,
    maintainability, algorithm and code efficiency.

    1) Create a class CardDeck() to provide the functionality of a deck of playing cards.
       Each card in the deck is represented by a non-mutable tuple string pair consisting of a suit
       (Spades, Hearts, Clubs, Diamonds) and a rank (2-10, Jack, Queen, King, Ace). For example: (‘Club’, ‘9’).

       Class operations should include:

          • available(card):    return true if card is in the deck
          • cards():            return a list of the remaining cards
          • count():            return remaining number of draws possible
          • draw(n):            return a list of the n cards. The n cards should be removed from the deck
          • shuffle():          initialize and randomize the order of future draws

       Here are a few recommendations/hints for one way to implement this class

          a) Review what functions the random library provides.
          b) Review what functions can be used on lists and tuples.
          c) Before creating a class definition experiment with code to create a deck of cards
             and perform the other functions.
          d) When shuffle() is called all cards are back in the deck (see the end of screen shot below)
          e) When a draw of cards is made, the cards might be removed from the deck or just made inaccessible for
             future operations. Making the card inaccessible might make it easier to implement the shuffle function.
          f) Create additional functions if needed. For example, I created a function test() that creates a deck,
             shuffles cards, draws cards and then prints out what cards I got.

    TURN IN: Along with your code, turn in a screen shot using the commands in the below screenshot.
             Note this sequence uses two libraries to display your username and the date/time.

       --------------------------------------------------------------------------------------
       |>>> from datetime import datetime                                                   |
       |>>> print (datetime.now().strfttime("%Y-%m-%d %H:%M:%S"))                           |
       |    2022-04-23 10:38:27                                                             |
       |>>> import os                                                                       |
       |>>> from datetime import datetime                                                   |
       |>>> os.getlogin()                                                                   |
       |    'tom16'                                                                         |
       |>>> print (datetime.now().strfttime("%Y-%m-%d %H:%M:%S"))                           |
       |    2022-04-23 10:38:59                                                             |
       |>>> deck = CardDeck()                                                               |
       |>>> deck.shuffle()                                                                  |
       |>>> hand = deck.draw(2)                                                             |
       |>>> hand                                                                            |
       |    [('Spade', '10'), ('Heart', '8')]                                               |
       |>>> deck.available( ('Space', '4') )                                                |
       |    True                                                                            |
       |>>> deck.available( ('Space', '10') )                                               |
       |    False                                                                           |
       |>>> hand2 = deck.draw(51)                                                           |
       |    Only 50 remaining                                                               |
       |>>> hand2 = deck.draw(44)                                                           |
       |>>> deck.cards()                                                                    |
       |    [('Spade', 'King'), ('Space', '5'), ('Club', '7'), ('Diamond', 'Ace'),          |
       |     ('Spade', 'Jack'), ('Heart', 'Queen')                                          |
       |>>> deck.count()                                                                    |
       |    6                                                                               |
       |>>> deck.shuffle()                                                                  |
       |>>> deck.count()                                                                    |
       |    52                                                                              |
       --------------------------------------------------------------------------------------

"""

import random

class CardDeck():
    """ Create a class CardDeck() to provide the functionality of a deck of playing cards.
    """

    # Class Attributes
    suits: [str]
    ranks: [str]
    deck: [()]

    suits = [ 'Heart', 'Diamond', 'Club', 'Spade']
    ranks = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King' ,'Ace']

    def __init__(self):
        """ Initialize a deck of cards - call shuffle()
        """
        self.shuffle()

    def available(self, card: (str, str)) -> bool:
        """ return true if card is in the deck
        :param card: a tuple representing the suit and rank of a card
        :type card: typle (str, str)
        :return: True or False
        :rtype: list of tupbles
        """
        return (card in self.deck)

    def cards(self) -> [()]:
        """ return a list of the remaining cards
        :return: cards
        :rtype: list of tuples
        """
        return self.deck

    def count(self) -> int:
        """ Get the count of the card deck
        :return: coutn of cards
        :rtype: int
        """
        return len(self.deck)

    def draw(self, n) -> [()]:
        """ deal out n number of cards from a deck
        :param n: number of cards to deal
        :type n: int
        :return: cards to be dealt
        :rtype: list of tuples
        """
        hand = self.deck[:n]
        self.deck = self.deck[n:]
        return (hand)

    def shuffle(self) -> [(str, str)]:
        """  initialize and randomize the order of future draws
        :return: shuffled deck of cards
        :rtype: [(str, str)]
        """
        self.deck = [tuple([s, r]) for s in self.suits for r in self.ranks]
        random.shuffle(self.deck)

