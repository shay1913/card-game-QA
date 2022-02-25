from unittest import TestCase
from unittest import mock
from game_cards.Player import Player
from game_cards.Card import Card
from game_cards.DeckOfCards import DeckOfCards



class TestPlayer(TestCase):
    def setUp(self):
        self.test_player = Player("Eli")  # set the player's name valid and number of cards is default=26

# ===================================================================================

    # Test a valid case of player name in __init__
    def test_valid__init__1(self):
        self.assertEqual(self.test_player.P_name, "Eli")  # test the player's name valid

    # Test a valid case of num of cards in __init__
    def test_valid__init__2(self):
        max_valid = Player("Shay",26)
        min_valid = Player("Dani",10)
        self.assertEqual(min_valid.P_num_of_cards, 10)  # test the num of cards is 10 valid
        self.assertEqual(max_valid.P_num_of_cards, 26)  # test the num of cards is 26 valid

    # test if num of card bigger than 26 or lower than 10 change to default 26
    def test_valid__init__3(self):
        roei_cards = Player("Roei",43)
        yael_cards = Player("Yael",4)
        self.assertEqual(roei_cards.P_num_of_cards, 26)
        self.assertEqual(yael_cards.P_num_of_cards, 26)

        # Test invalid parameters sent to __init__
    def test_invalid__init__(self):
        # invalid name
        with self.assertRaises(TypeError):
            invalid_test_player1 = Player(123)  # test that name of player can't be int!
        # Invalid num of cards as str
        with self.assertRaises(TypeError):
            invalid_test_player2 = Player("Shay", "abc")  # test that num of cards can't be str!

# ===================================================================================

    # Test that set_hand is valid and divide cards to players
    def test_set_hand(self):
        deck = DeckOfCards()
        self.assertEqual(len(self.test_player.P_cards),0)
        self.test_player.set_hand(deck)
        self.assertEqual(len(self.test_player.P_cards),26)

    # Checks that the dealt card from the deck is in Player's hand
    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one',return_value = Card(2,5))
    def test_set_hand2(self,mock_deal_one):
        player = Player("Yoni",10)
        deck = DeckOfCards()
        player.set_hand(deck)
        self.assertEqual(player.P_cards.count(Card(2,5)),10)  # Check that the dealt card is in Player's hand

# ===================================================================================

    # Test that random card pulls out from player's deck of cards
    def test_get_card(self):
        deck = DeckOfCards()
        self.test_player.set_hand(deck)
        self.assertEqual(len(self.test_player.P_cards),26)
        self.test_player.get_card()
        self.assertEqual(len(self.test_player.P_cards),25)

# ===================================================================================

