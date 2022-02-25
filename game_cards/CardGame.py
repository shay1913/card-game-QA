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

    """A method that shuffle the deck and deal the cards to the players"""
    def new_game(self):
        # the method can only start once
        count_new_game = 0
        if count_new_game == 0:
            self.deck.card_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
            count_new_game += 1
        else:
            print("Error! game already started")
            return

    """A method that will present the winning player from the players"""
    def get_winner(self):
        if len(self.player1.P_cards)>len(self.player2.P_cards):
            return self.player1

        elif len(self.player1.P_cards)<len(self.player2.P_cards):
            return self.player2
        else:
            return None   # if the game ended in tie, the method return None
