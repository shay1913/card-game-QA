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