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

    # Testing invalid suit not in range 1-4 and value not in range 2-14
    def test_invalid__init__2(self):
        with self.assertRaises(ValueError):
            invalid_suit_range = Card(5, 3)
        with self.assertRaises(ValueError):
            invalid_suit_range = Card(-1, 3)
        with self.assertRaises(ValueError):
            invalid_value_range = Card(2, 15)
        with self.assertRaises(ValueError):
            invalid_value_range = Card(2, 1)

    # Checks __gt__ method basic behaviour
    def test_valid__gt__(self):
        card2 = Card(2,4)
        card3 = Card(1,8)
        card4 = Card(3,6)
        card5 = Card(1,6)
        self.assertGreater(self.card,card2)  # Test that the value of main card bigger than value of card2
        self.assertGreater(card3,self.card)  # Test that the value of card3 bigger than value of main card
        self.assertGreater(self.card,card4)  # Test that the suit of main card bigger than suit of card4
        self.assertGreater(card5,self.card)  # Test that the suit of card5 bigger than suit of main card

    # Test invalid other card in __gt__
    def test_invalid__gt__invalid_card(self):
        with self.assertRaises(TypeError):
            invalid_card = Card(2, "aff")  # the value of other card must be type of int!
            self.assertGreater(self.card,invalid_card)
        with self.assertRaises(TypeError):
            invalid_suit = Card("avv",6)  # the suit of other card must be type of int!
            self.assertGreater(self.card,invalid_suit)

    # Checks __eq__ method basic behaviour
    def test__eq__valid(self):
        six_of_spade = Card(2, 6)
        ten_of_heart = Card(3,10)
        self.assertTrue(self.card == six_of_spade)  # The same card
        self.assertFalse(six_of_spade == ten_of_heart)  # Not the same card