from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        # creates a deck of cards
        self.deck_test = DeckOfCards()

    def test_valid__init__(self):
        self.assertTrue(type(self.deck_test.all_cards)==list)  # test that the type of all cards is list
        self.assertEqual(len(self.deck_test.all_cards),52)  # test that the list of all cards is 52 cards
        for card in self.deck_test.all_cards:
            self.assertEqual(self.deck_test.all_cards.count(card),1)  # test that the card in list of all cards only 1 time

    # test that the deck of cards after shuffle is valid
    def test_card_shuffle(self):
        test_list1 = DeckOfCards()
        self.deck_test.card_shuffle()
        self.assertNotEqual(test_list1.all_cards, self.deck_test.all_cards)

    # test validation of deal_one by compare 2 lists before and after
    def test_deal_one(self):
        test_list1 = DeckOfCards()
        self.deck_test.deal_one()
        self.assertNotEqual(test_list1.all_cards, self.deck_test.all_cards)

    # test validation of deal_one by compare len of 2 lists before and after
    def test_deal_one2(self):
        test_list1 = DeckOfCards()
        self.assertEqual(len(test_list1.all_cards),len(self.deck_test.all_cards))

        self.assertNotEqual(len(test_list1.all_cards),len(self.deck_test.all_cards))

    # tests that the method not giving any card when the deck is empty, and return a message
    def test_deal_one3(self):
        test_list1 = DeckOfCards()
        test_list1.all_cards = []
        test_list1.deal_one()