from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player
from game_cards.CardGame import CardGame
from game_cards.Card import Card

class TestCardGame(TestCase):
    def setUp(self):
        self.test_war_game = CardGame("shay","or",10)

    def test_valid__init__(self):
        self.assertEqual(self.test_war_game.player1.P_name,"shay")
        self.assertEqual(self.test_war_game.player2.P_name,"or")
        self.assertEqual(self.test_war_game.player1.P_num_of_cards,10)
        self.assertEqual(self.test_war_game.player2.P_num_of_cards,10)

    #check that num of cards is defult 26
    def test_valid__init__2(self):
        min_num_of_cards_game = CardGame("or","eli",9)
        max_num_of_cards_game = CardGame("or","eli",27)
        self.assertEqual(min_num_of_cards_game.player1.P_num_of_cards,26)
        self.assertEqual(min_num_of_cards_game.player2.P_num_of_cards,26)
        self.assertEqual(max_num_of_cards_game.player1.P_num_of_cards, 26)
        self.assertEqual(max_num_of_cards_game.player2.P_num_of_cards, 26)


    def test_invalid__init__(self):
        with self.assertRaises(TypeError):
            invalid_player1_game = CardGame(13,"omer",26)
        with self.assertRaises(TypeError):
            invalid_player2_game = CardGame("omer",12,26)

        with self.assertRaises(TypeError):
            invalid_num_of_cards_game = CardGame("efi","omer","asdss")

    #test that after new_game started the number of cards in the deck updated
    def test_new_game(self):
        self.assertEqual(len(self.test_war_game.player1.P_cards),10)
        self.assertEqual(len(self.test_war_game.player2.P_cards),10)
        self.assertEqual(len(self.test_war_game.deck.all_cards),32)

    def test_new_game2(self):
        self.test_war_game.new_game()
        self.assertEqual(len(self.test_war_game.player1.P_cards),10)
        self.assertEqual(len(self.test_war_game.player2.P_cards),10)
        self.assertEqual(len(self.test_war_game.deck.all_cards),32)