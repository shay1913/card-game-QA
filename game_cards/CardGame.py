from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player

class CardGame:
    """A method that gets the names of the players, and the number of cards for each player"""
    def __init__(self,player1:str,player2:str,num_of_cards=26):
        # the fixing for test_invalid__init__
        if type(player1) != str or type(player2) != str:
            raise TypeError("name must be str type")

        if type(num_of_cards) != int:
            raise TypeError("num of cards must be int type")

        # if the players num of cards not in range 10-26 ,player's num of card is default 26
        if 10 > num_of_cards or num_of_cards > 26:
            num_of_cards = 26

        self.deck = DeckOfCards()
        self.player1 = Player(player1,num_of_cards)
        self.player2 = Player(player2,num_of_cards)
        self.new_game()


