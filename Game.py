from Player import *
from Dealer import *


class Game:
    def __init__(self):
        self.outcome = ""
        self.score = [0, 0]


def show_score(player_score, dealer_score):
    """
    Prints a score board containing each player's score
    :param player_score: int Player.score
    :param dealer_score: int Dealer.score
    :return: void(Prints a score board)
    """
    print("Current Score")
    print("-------------")
    print("Player:", player_score)
    print("Dealer:", dealer_score)


def start_round():
    """
    Sets up a round
    Assigns both players two cards then then calls Deck.deal_starting_hand()
    to animate the dealing
    """
    print(chr(27) + "[2J")
    print("New Blackjack round starting!\n")

    # Assigns both players two random cards
    for i in range(0, 2):
        current_player.hand.append(deck.get_random_card())
        dealer.hand.append(deck.get_random_card())

    dealer.hand_value = deck.hand_value(dealer.hand)
    current_player.hand_value = deck.hand_value(current_player.hand)
    sleep(1)
    deck.deal_starting_hand(dealer.hand, current_player.hand, current_game.score)


def determine_outcome(player_hand, dealer_hand, bust_status):
    # =======================
    # Game outcome Conditions
    # =======================
    if dealer_hand > 21 and bust_status:
        current_game.outcome = "Both players have bust, dealer wins"
        dealer.score += 1
        current_player.score += 1

    elif dealer_hand > 21 and not bust_status:
        current_game.outcome = "Dealer has bust, you win!"
        current_player.score += 1

    elif (player_hand > dealer_hand) and not bust_status:
        # Added for flavor
        if player_hand == 21:
            current_game.outcome = "Blackjack!"
        else:
            current_game.outcome = "You win!"
        current_player.score += 1

    elif dealer_hand == player_hand:
        current_game.outcome = "Tie"
        current_player.score += 1
        dealer.score += 1

    else:
        if dealer_hand is 21:
            current_game.outcome = "Dealer got blackjack!"
        else:
            current_game.outcome = "Dealer wins"
        dealer.score += 1


if __name__ == '__main__':
    print(chr(27) + "[2J")
    print("========================\n"
          "| Blackjack Assessment |\n"
          "|   By: Joshua Irwin   |\n"
          "========================\n")
    sleep(1)

    current_game = Game
    current_player = Player()
    dealer = Dealer()
    deck = Deck()
    keep_playing = True
    while keep_playing is True:
        # Clear the lists in deck to allow past cards to come back into play, essentially reshuffling
        # the entire deck back into the game.
        deck.used_card = []
        deck.used_suit = []

        # Clear each player's hand
        current_player.hand = []
        dealer.hand = []

        player_has_bust = False
        player_dealt_blackjack = False
        start_round()

        show_score(current_player.score, dealer.score)

        print("                     =================")
        print("                         Your Turn                    ")
        print("                     =================")
        print("Dealer's Hand:", dealer.hand_value)
        deck.show_hand(dealer.hand)
        deck.show_hand(current_player.hand)
        player_has_passed = False

        if type(current_player.hand_value) is tuple:
            if current_player.hand_value[1] is 21:
                print("Your Hand:", current_player.hand_value[1])
                current_game.outcome = "Winner Winner Chicken Dinner!"
                current_player.score += 1
                player_dealt_blackjack = True

        print("Your Hand:", current_player.hand_value)
        if type(dealer.hand_value) is tuple:
            if dealer.hand_value[1] is 21:
                current_game.outcome = "Dealer dealt blackjack!"
                player_dealt_blackjack = True
                dealer.score += 1

        while not (player_has_passed or player_has_bust or player_dealt_blackjack):
            player_has_passed = current_player.handle_player_choice(deck)
            print(chr(27) + "[2J")
            show_score(current_player.score, dealer.score)
            print("                     =================")
            print("                         Your Turn                    ")
            print("                     =================")
            print("Dealer's Hand:", dealer.hand_value)
            deck.show_hand(dealer.hand)
            deck.show_hand(current_player.hand)
            print("Your Hand: ", current_player.hand_value)

            if deck.hand_value(current_player.hand) is 21:
                current_game.outcome = "Blackjack!"
                current_player.score += 1
                player_dealt_blackjack = True

            elif type(current_player.hand_value) is not tuple and current_player.hand_value >= 21:
                print("Bust!")
                sleep(1)
                player_has_bust = True

        # Dealers turn
        # Check if 21
        if not player_dealt_blackjack:
            dealer.play_round(deck, current_player.hand, current_player.score)
            determine_outcome(current_player.hand_value, dealer.hand_value, player_has_bust)

        print(chr(27) + "[2J")
        show_score(current_player.score, dealer.score)
        print("                     ==================")
        print("                         Round Over                   ")
        print("                     ==================")
        print("Dealer's Hand:", dealer.hand_value)
        deck.show_hand(dealer.hand)
        deck.show_hand(current_player.hand)
        print("Your Hand:", current_player.hand_value)
        print(current_game.outcome)
        player_input = input("Play again? [Y/n]")
        if player_input.lower() == 'n':
            print("Good bye")
            sleep(1)
            keep_playing = False
