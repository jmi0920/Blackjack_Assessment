import unittest
from Deck import *
from Player import *
from Dealer import *


class GameTest(unittest.TestCase):
    def test_show_score(self):
        test_dealer = Dealer()
        test_player = Player()

        test_dealer.score = 0
        test_player.score = 2

        self.assertEqual(
            "Current Score\n" +
            "-------------\n" +
            "Player:" + str(test_player.score) + "\n" +
            "Dealer:" + str(test_dealer.score) + "\n",

            "Current Score\n" +
            "-------------\n" +
            "Player:" + str(2) + "\n" +
            "Dealer:" + str(0) + "\n"
        )

    def test_start_round(self):
        test_dealer = Dealer()
        test_player = Player()
        test_deck = Deck()

        for i in range(0, 2):
            test_player.hand.append(test_deck.get_random_card())
            test_dealer.hand.append(test_deck.get_random_card())

        self.assertEqual(len(test_player.hand), 2)
        self.assertEqual(len(test_dealer.hand), 2)

        for x in range(0, 2):
            self.assertEqual(type(test_player.hand[x]), tuple)
            self.assertEqual(type(test_dealer.hand[x]), tuple)

    def test_determine_outcome(self):
        pass


if __name__ == '__main__':
    unittest.main()
