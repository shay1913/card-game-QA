from unittest import TestCase
from game_cards.Card import Card

class TestCard(TestCase):
    # Testing suit and value of the card
    def setUp(self):
        self.card = Card(2,6)

    # Testing valid __init__
    def test_valid__init__(self):
        self.assertEqual(self.card.suit,2)  # test that the suit of card valid
        self.assertEqual(self.card.value,6)  # test that the value of card valid

    # Testing invalid suit and value as str
    def test_invalid__init__(self):
        with self.assertRaises(TypeError):  # test suit as str
            invalid_suit = Card("af",7)
        with self.assertRaises(TypeError):  # test value as str
            invalid_value = Card(1,"ggs")