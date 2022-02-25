"""class that represent a card in card game"""
class Card:
    """a method that shows how card is build"""
    def __init__(self,suit,value):

        # the fixing for test_invalid__init__2
        if type(suit)!=int:
            raise TypeError("Card type must be int")
        if type(value)!=int:
            raise TypeError("Card type must be int")

        # the fixing for test_invalid__init__3
        if 1>suit or suit>4:
            raise ValueError("the suit not in right range")
        if 2>value or value>14:
            raise ValueError("the value not in right range")

        self.suit = suit
        self.value = value

    """a method that compering two cards and return the bigger card"""
    def __gt__(self, other):
        if type(other.value)!=int:
            raise TypeError("Card type must be int")
        if type(other.suit)!=int:
            raise TypeError("Card type must be int")
        if self.value>other.value:
            return True
        if self.value == other.value:
            if self.suit<other.suit:
                return True
            else:
                return False
        else:
            return False