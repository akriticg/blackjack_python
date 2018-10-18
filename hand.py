

class Hand:
    """A blackjack hand"""
    def __init__(self):
        self.number_of_aces = 0
        self.cards = []

    def receive_card(self, card):
        if card.value == "ace":
            self.number_of_aces += 1
        self.cards.append(card)
    '''
    def score(self):
        s = sum([c.num_value() for c in self.cards])
        if s > 21:
            s = s - self.number_of_aces * 10
        return s
    '''

    def score(self):
        s = sum([c.num_value() for c in self.cards])
        while s > 21 and self.number_of_aces > 0:
            s = s - 10
            self.number_of_aces -= 1

        return s

    def display(self):
        print("Player hand:")
        for c in self.cards:
            print("\tThe", c.value, "of", c.suit)
