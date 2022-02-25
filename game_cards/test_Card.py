from unittest import TestCase
from game_cards.Card import Card

class TestCard(TestCase):
    # Testing suit and value of the card
    def setUp(self):
        self.card = Card(2,6)