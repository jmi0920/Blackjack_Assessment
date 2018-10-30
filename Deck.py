import random
from time import sleep


class Deck:
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    # Allows printing of suit unicode when called
    suits_unicode = [u"\u2660", u"\u2666", u"\u2764", u"\u2663"]
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    def __init__(self):
        """
        Initalize the deck object with an empty list for cards that have been used in a game.
        """
        self.used_cards = []

    def get_random_card(self):
        """
        Gets a random card value when called that has not been seen in the game already.
        :return: a tuple containing (suits[n], cards[x]) where n,x are random values that have not currently
        been used together.
        """
        valid_card = False
        while valid_card is False:
            random_card = (random.randint(0, 3), random.randint(0, 12))
            # If the card is contained in used_cards, then draw a new card
            if random_card in self.used_cards:
                pass
            # If card has not been seen this game, add it to the used_card List and return it, adding it
            # to a players hand
            else:
                self.used_cards.append(random_card)
                return random_card

    def hand_value(self, current_hand):
        """
        Calculates the value of the current hand, returns a tuple if there are two possible values
        :param current_hand: A List containing two tuples that are mapped to (suits[n], cards[x])
        :return: A tuple if the hand contains an Ace and if the combination of the Ace and other cards are not > 10
                 OR an integer
        """
        current_score = 0
        ace_count = 0
        for i in range(0, len(current_hand)):
            if type(self.cards[current_hand[i][1]]) == int:
                current_score += self.cards[current_hand[i][1]]
            else:
                if self.cards[current_hand[i][1]] == "Ace":
                    ace_count += 1
                else:
                    current_score += 10

        if ace_count > 0:
            if current_score <= 10:
                return  current_score + (ace_count * 1), current_score + 11 + ((ace_count-1) * 1)
            else:
                return current_score + (ace_count * 1)
        else:
            return current_score

    def deal_starting_hand(self, dealer_hand, player_hand, scores):
        """
        Animates each player being dealt cards
        :param dealer_hand: A List containing two tuples that are mapped to (suits[n], cards[x])
        :param player_hand: A List containing two tuples that are mapped to (suits[n], cards[x])
        :param scores: A List mapped to [player_score, dealer_score]
        :return: void(Prints out to console)
        """
        # Print top left
        print(chr(27) + "[2J")
        print("Current Score")
        print("-------------")
        print("Player:", scores[0])
        print("Dealer:", scores[1])
        print("                     ===================")
        print("                          Dealing.")
        print("                     ===================")
        self.show_card(dealer_hand[0][0], dealer_hand[0][1])
        print("\n"*13)
        sleep(1)
        print(chr(27) + "[2J")
        print("Current Score")
        print("-------------")
        print("Player:", scores[0])
        print("Dealer:", scores[1])
        print("                     ===================")
        print("                          Dealing..")
        print("                     ===================")
        self.show_card(dealer_hand[0][0], dealer_hand[0][1])
        self.show_card(player_hand[0][0], player_hand[0][1])
        sleep(1)
        print(chr(27) + "[2J")
        print("Current Score")
        print("-------------")
        print("Player:", scores[0])
        print("Dealer:", scores[1])
        print("                     ===================")
        print("                          Dealing...")
        print("                     ===================")
        # Print Top left and Bottom left
        self.show_hand(dealer_hand)
        self.show_card(player_hand[0][0], player_hand[0][1])
        sleep(1)
        print(chr(27) + "[2J")

    def show_hand(self, current_hand):
        """
        :param current_hand: A 2 dimensional array containing arrays of length 2 mapping to [suit[n], card[n]]
        :return: Prints out all cards in a players hand side by side
        """

        print("--------------------  " * len(current_hand))

        for i in range (0, len(current_hand)):
            card_value = self.cards[current_hand[i][1]]
            if type(card_value) is str:
                card_value = card_value[0].upper()

            if type(card_value) == int and card_value < 10 or type(card_value) == str:
                print(f'| {card_value}{self.suits_unicode[current_hand[i][0]]}               |  ',  end="")
            else:
                print(f'| {card_value}{self.suits_unicode[current_hand[i][0]]}              |  ', end="")

        # Print new line to account for end=""
        print()
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))
        print("|                  |  " * len(current_hand))

        for i in range (0, len(current_hand)):
            card_value = self.cards[current_hand[i][1]]
            if type(card_value) is str:
                card_value = card_value[0].upper()

            if type(card_value) == int and card_value < 10 or type(card_value) == str:
                print(f'|               {card_value}{self.suits_unicode[current_hand[i][0]]} |  ', end="")
            else:
                print(f'|              {card_value}{self.suits_unicode[current_hand[i][0]]} |  ', end="")
        # Print new line to account for end=""
        print()

        print("--------------------  " * len(current_hand))

    def show_card(self, suit_in, card_in):
        """
        :param card_in: The card card value mapping to cards[]
        :param suit_in: The cards suit value, mapping to suits[]
        :return: Prints out a singular card to the terminal
        """
        if type(self.cards[card_in]) is str:
            card_in = self.cards[card_in][0].upper()
        else:
            card_in += 1
        print("--------------------")
        if type(card_in) == int and card_in < 10 or type(card_in) == str:
            print(f'| {card_in}{self.suits_unicode[suit_in]}               |  ')
        else:
            print(f'| {card_in}{self.suits_unicode[suit_in]}              |  ')
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        if type(card_in) == int and card_in < 10 or type(card_in) == str:
            print(f'|               {card_in}{self.suits_unicode[suit_in]} |  ')
        else:
            print(f'|              {card_in}{self.suits_unicode[suit_in]} |  ')
        print("--------------------")

    @staticmethod
    def face_down_card():
        """
        Prints a face down card
        :return: Prints a face down card to the console.
        """
        print("--------------------")
        print("|/ / / / / / / / / |")
        print("| / / / / / / / / /|")
        print("|/ / / / / / / / / |")
        print("| / / / / / / / / /|")
        print("|/ / / / / / / / / |")
        print("| / / / / / / / / /|")
        print("|/ / / / / / / / / |")
        print("| / / / / / / / / /|")
        print("|/ / / / / / / / / |")
        print("| / / / / / / / / /|")
        print("--------------------")