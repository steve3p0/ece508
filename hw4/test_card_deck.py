from unittest import TestCase

import card_deck


class TestCardDeck(TestCase):
    """ Class to test CardDeck
    """

    def test_integration(self):
        """ Test created to test intntegration
        :return: None
        :rtype: None
        """

        from datetime import datetime
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        import os
        print(f"user: {os.getlogin()}")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        deck = card_deck.CardDeck()
        deck.shuffle()
        hand = deck.draw(2)
        print(f"hand: {hand}")
        print(f"available: {deck.available( ('Spade', '4') ) }")
        print(f"available: {deck.available( ('Spade', '10') )}")
        hand2 = deck.draw(51)
        hand2 = deck.draw(44)

        hand2 = deck.draw(5)
        hand2 = deck.draw(10)

        # I think there is a problem with this code taking too many cards
        # hand2 = deck.draw(51)
        # hand2 = deck.draw(44)

        print(f"remaining cards: {deck.cards()}")
        print(f"deck count: {deck.count()}")
        deck.shuffle()
        print(f"deck count: {deck.count()}")
