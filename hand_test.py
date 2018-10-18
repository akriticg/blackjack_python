from hand import Hand
from card import Card


def main():
    test_hand_score()


def test_hand_score():
    hand = Hand()
    hand.receive_card(Card("hearts", "9"))
    hand.receive_card(Card("hearts", "ace"))
    hand.receive_card(Card("spades", "ace"))
    print(hand.score())

main()
