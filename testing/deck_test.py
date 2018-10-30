import unittest
from Deck import *


class DeckTest(unittest.TestCase):

    def test_get_random_card(self):
        test_deck = Deck()
        # Go through all possible cards in the deck
        for i in range(0, 52):
            test_deck.get_random_card()

        # Verify that the set of used_cards is equal to 52, thus every card is unique
        self.assertEqual(len(set(test_deck.used_cards)), 52)

    def test_hand_value(self):
        test_deck = Deck()
        # Test to non face cards
        test_player_hand = [(2,3), (3, 4)]
        self.assertEqual(test_deck.hand_value(test_player_hand), 9)

        # Test face card and Ace
        test_player_hand = [(0, 0), (0, 12)]
        self.assertEqual(test_deck.hand_value(test_player_hand), (11, 21))

    def test_show_card(self):
        test_deck = Deck()
        card_in = 3
        suit_in = 0
        self.assertEqual(
            "--------------------\n" +
            f'| {card_in}{test_deck.suits_unicode[suit_in]}               |  \n' +

            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            f'|               {card_in}{test_deck.suits_unicode[suit_in]} |  \n' +
            "--------------------",

            "--------------------\n" +
            f'| {3}\u2660               |  \n' +

            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            "|                  |\n" +
            f'|               {3}\u2660 |  \n' +
            "--------------------"
        )
