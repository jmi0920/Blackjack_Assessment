import random

class Card:
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    # TODO Make sure align correctly
    suits_unicode = [u"\u2666", u"\u2660", u"\u2764", u"\u2663"]
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    used_suit = []
    used_card = []

    def __init__(self, suit_id, card_id):
        self.card = card_id
        self.suit = suit_id

    def get_random_card(self):
        valid_card = False
        while valid_card is False:
            random_suit = random.randint(0, 3)
            random_card = random.randint(0, 12)

            for i in range(0, len(self.used_suit)):
                if random_suit == self.used_suit[i] and random_card == self.used_card[i]:
                    random_suit = random.randint(0, 3)
                    random_card = random.randint(0, 12)
            else:
                self.used_card.append(random_card)
                self.used_suit.append(random_suit)
                self.suit = random_suit
                self.card = random_card
                valid_card = True

    def get_suit(self):
        return self.suits[self.suit]

    def get_card(self):
        return str(self.cards[self.card]) + " of " + str(self.suits[self.suit])

    def print_card(self):
        if type(self.cards[self.card]) is str:
            self.card = self.cards[self.card][0].upper()
        else:
            self.card += 1
        print("--------------------")
        if type(self.card) == int and self.card < 10 or type(self.card) == str:
            print(f'| {self.card}{self.suits_unicode[self.suit]}               |  ')
        else:
            print(f'| {self.card}{self.suits_unicode[self.suit]}              |  ')
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
        if type(self.card) == int and self.card < 10 or type(self.card) == str:
            print(f'|               {self.card}{self.suits_unicode[self.suit]} |  ')
        else:
            print(f'|              {self.card}{self.suits_unicode[self.suit]} |  ')
        print("--------------------")


if __name__ == '__main__':
    t = Card(0, 0)
    for i in range(0, 10):
        t.get_random_card()
        print(t.get_card())
        t.print_card()


