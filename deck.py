import random as r
from card import Card


class Deck:
    """A standard deck of playing cards"""
    def __init__(self):
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        values = ['ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'jack', 'queen', 'king']
        self.cards = self.shuffle([Card(suit, value)
                                   for suit in suits
                                   for value in values])

    def shuffle(self, cards):
        list_range = range(0, len(cards))
        for i in list_range:
            j = r.randint(list_range[0], list_range[-1])
            cards[i], cards[j] = cards[j], cards[i]
        return cards

    def deal_one(self):
        return self.cards.pop()
