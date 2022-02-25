from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.Player import Player
from game_cards.CardGame import CardGame
player1 = input("enter player name: ")
player2 = input("enter player name: ")
card_deck = DeckOfCards()
war_game = CardGame(player1,player2,26)
print(f"{player1},\n{war_game.player1.P_cards}")
print(f"{player2},\n{war_game.player2.P_cards}")
