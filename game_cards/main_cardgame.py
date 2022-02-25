from game_cards.DeckOfCards import DeckOfCards
from game_cards.CardGame import CardGame
player1 = input("enter player name: ")
player2 = input("enter player name: ")
card_deck = DeckOfCards()
war_game = CardGame(player1,player2,26)
print(f"{player1},\n{war_game.player1.P_cards}")
print(f"{player2},\n{war_game.player2.P_cards}")

for i in range(10):
    card1 = war_game.player1.get_card()
    card2 = war_game.player2.get_card()

    if card1 > card2:
        war_game.player1.add_card(card1)
        war_game.player1.add_card(card2)
        print(f"{player1}:{card1}")
        print(f"{player2}:{card2}")
        print(f"{player1} win the round")

    if card1 < card2:
        war_game.player2.add_card(card1)
        war_game.player2.add_card(card2)
        print(f"{player1}:{card1}")
        print(f"{player2}:{card2}")
        print(f"{player2} win the round")

print("#######################################################")

print(war_game.get_winner())
if war_game.get_winner()== None:
    print("The game ended in tie")