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

    """A method that randomly shuffles the list of cards"""
    def card_shuffle(self):
        shuffle(self.all_cards)

    """A method of pulling one random card out of the deck"""
    def deal_one(self):
        # when the deck of cards is empty , the function not giving a card
        if len(self.all_cards)>0:
            card = self.all_cards.pop()
            return card
        else:
            print("There is no cards to give")

    def __repr__(self):
        return f"{self.all_cards}"