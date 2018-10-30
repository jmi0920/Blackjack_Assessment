from Deck import *
from time import sleep


class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.score = 0

    def play_round(self, deck, final_player_hand, player_score):
        """

        :param deck: A 2 dimensional array containing arrays of length 2 mapping to [suit[n], card[n]]
        :param final_player_hand: The final hand the player has chosen to stand with
        :return:
        """
        # If tuple due to Ace in hand, take the highest value and set to hand value
        if type(self.hand_value) is tuple:
            print("True")
            self.hand_value = self.hand_value[1]

        while self.hand_value < 17:
            sleep(1)
            print(chr(27) + "[2J")
            print("Current Score")
            print("-------------")
            print("Player:", player_score)
            print("Dealer:", self.score)
            self.hand.append(deck.get_random_card())
            self.hand_value = deck.hand_value(self.hand)
            print("                     =====================")
            print("                         Dealer's Turn                    ")
            print("                     =====================")
            print("Dealer's Hand:", deck.hand_value(self.hand))
            deck.show_hand(self.hand)
            deck.show_hand(final_player_hand)
            print("Your Hand: ", deck.hand_value(final_player_hand))

            if type(self.hand_value) is tuple:
                self.hand_value = self.hand_value[1]

        sleep(1)
        # If dealer stands with an ace in that is registering as a tuple still (i.e., Face Card and Ace),
        # set hand value to max possible value
        if type(self.hand_value) is tuple:
            self.hand_value = self.hand_value[1]
        print("Dealer stays")

