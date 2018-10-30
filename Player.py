class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.score = 0

    def handle_player_choice(self, current_deck):
        while True:
            player_input = input("Options\n"
                  "\t1: Hit\n"
                  "\t2: Stand\n"
                  "What would you like to do:")

            if player_input is '1' or player_input is '2':
                if player_input is '1':
                    self.hand.append(current_deck.get_random_card())
                    self.hand_value = current_deck.hand_value(self.hand)
                    return False

                else:
                    # If player stands with an ace in that is registering as a tuple still (i.e., Face Card and Ace),
                    # set hand value to max possible value
                    if type(self.hand_value) is tuple:
                        self.hand_value = self.hand_value[1]
                    return True
            else:
                print("That is an invalid response!")
