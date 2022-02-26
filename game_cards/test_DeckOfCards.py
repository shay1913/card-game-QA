from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        # creates a deck of cards
        self.deck_test = DeckOfCards()

    # Test the __init__ method, that the list contains 52 items, and that the items are not the same card
    def test__init__valid(self):
        self.assertTrue(len(self.deck_of_cards.deck) == 52)
        for suit in range(1, 5):
            for value in range(1, 14):
                card = Card(value, suit)
                exist = False
                for item in self.deck_of_cards.deck:
                    if item.get_name() == card.get_name() and exist is False:
                        exist = True
                self.assertTrue(exist)

    # Test that the deck of cards after shuffle is valid
    def test_card_shuffle(self):
        test_list1 = DeckOfCards()
        self.deck_test.card_shuffle()
        self.assertNotEqual(test_list1.all_cards, self.deck_test.all_cards)

    # Test validation of deal_one by compare 2 lists before and after
    def test_deal_one(self):
        test_list1 = DeckOfCards()
        self.deck_test.deal_one()
        self.assertNotEqual(test_list1.all_cards, self.deck_test.all_cards)

    # Test validation of deal_one by compare len of 2 lists before and after
    def test_deal_one2(self):
        test_list1 = DeckOfCards()
        self.assertEqual(len(test_list1.all_cards),len(self.deck_test.all_cards))

        self.assertNotEqual(len(test_list1.all_cards),len(self.deck_test.all_cards))

    # Test that the method not giving any card when the deck is empty, and return a message
    def test_deal_one3(self):
        test_list1 = DeckOfCards()
        test_list1.all_cards = []
        test_list1.deal_one()