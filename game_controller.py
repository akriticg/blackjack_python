import random as r
import sys
from deck import Deck
from hand import Hand


class GameController:
    """A controller for a simple blackjack game"""
    def __init__(self):
        self.deck = Deck()
        self.dealer_score = r.randint(17, 21)
        self.player_hand = Hand()

    def start_play(self):
        print("The dealer's score is", self.dealer_score)
        self.deal_two()
        self.display_hand()
        self.stay_or_hit(input("Would you like to stay or hit?\n"))

    def deal_two(self):
        self.player_hand.receive_card(self.deck.deal_one())
        self.player_hand.receive_card(self.deck.deal_one())

    def display_hand(self):
        self.player_hand.display()

    def stay_or_hit(self, s_or_h):
        if s_or_h == "hit":
            self.player_hand.receive_card(self.deck.deal_one())
            self.display_hand()
            if self.player_is_bust():
                self.do_bust()
            elif self.player_hand.score() > self.dealer_score:
                print("You Win!!!")
            else:
                self.stay_or_hit(input("Would you like to stay or hit?\n"))
        elif s_or_h == "stay":
            self.do_stay()
        else:
            self.stay_or_hit(input("Would you like to stay or hit?\n"))

    def player_is_bust(self):
        return self.player_hand.score() > 21

    def do_stay(self):
        if self.player_hand.score() > self.dealer_score:
            print("You Win!!!")
        elif self.player_hand.score() < self.dealer_score:
            print("You lose.")
        else:
            print("You tied.")
        sys.exit()

    def do_bust(self):
        print("*********************************")
        print("***          BUST!            ***")
        print("*********************************\n")
        sys.exit()
