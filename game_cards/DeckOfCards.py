from game_cards.Card import Card
from random import shuffle
class DeckOfCards:
    """A method that creates a complete deck of 52 different cards,13 cards from each suit"""
    def __init__(self):
        self.all_cards = []

        for suit in range(1,5):
            for value in range(2,15):
                new_card = Card(suit, value)
                self.all_cards.append(new_card)