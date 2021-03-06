from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card

class Player:
    """A method that gets the player name, and his number of cards"""
    def __init__(self, P_name, P_num_of_cards = 26):

        # the fixing for test_invalid__init__
        if type(P_name) != str:
            raise TypeError("Name of player must be type of str!")
        if type(P_num_of_cards) != int:
            raise TypeError("Num of cards must be type of int!")

        if 10 > P_num_of_cards or P_num_of_cards > 26:
            P_num_of_cards = 26

        self.P_name = P_name
        self.P_cards = []
        self.P_num_of_cards = P_num_of_cards

    """A method that gets deck of cards, and split random cards for each player,
     according to the game cards number"""
    def set_hand(self, deck: DeckOfCards):
        for i in range(self.P_num_of_cards):
            self.P_cards.append(deck.deal_one())

    """A method that pulls random card from the player's deck of cards and return it"""
    def get_card(self):
        return self.P_cards.pop()

    """A method that receives card and adding it to the player's deck of cards"""
    def add_card(self,card: Card):
        # the fix for test invalid_add_card
        if type(card)!=Card:
            raise TypeError("value must be type Card")

        self.P_cards.append(card)

    def __repr__(self):
        return f"{self.P_name}"