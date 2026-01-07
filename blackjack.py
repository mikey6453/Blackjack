import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    # when a deck class is created, add the cards and shuffle them

    def __init__(self):
        cards = []

        for suit in SUITS:
            for rank in RANKS:
                card = Card(rank, suit)
                cards.append(card)

        self._cards = cards
    
    
deck = Deck()
print(len(deck._cards))