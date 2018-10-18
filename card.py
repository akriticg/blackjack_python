
class Card:
    """A playing card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def num_value(self):
        if self.value == "ace":
            return 11
        elif (self.value == "jack" or
              self.value == "queen" or
              self.value == "king"):
            return 10
        else:
            return int(self.value)
