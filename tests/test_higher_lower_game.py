import unittest
from unittest.mock import patch
from src.higher_lower_game import HigherLowerGame
from src.players.player import Player, ComputerPlayer
from src.card import Card, Deck

class TestHigherLowerGame(unittest.TestCase):
    def test_create_player(self):
        game = HigherLowerGame(["A", "Computer(easy)"], False)
        self.assertIsInstance(game.players[0], Player)
        self.assertIsInstance(game.players[1], ComputerPlayer)
        self.assertEqual(game.players[1].strategy.accuracy, 0.5)

    def test_evaluate_guess(self):
        game = HigherLowerGame(["A"], False)
        game.current_card = Card("7", "Hearts")
        next_card = Card("8", "Spades")
        player = game.players[0]
        self.assertTrue(game.evaluate_guess(player.higher_key, next_card))
        self.assertFalse(game.evaluate_guess(player.lower_key, next_card))

    def test_display_winner(self):
        game = HigherLowerGame(["A", "B"], False)
        game.players[0].add_score(10)
        game.players[1].add_score(5)
        with patch("builtins.print") as mock_print:
            game.display_winner()
            mock_print.assert_any_call("The winner is A with 10 points!")

if __name__ == "__main__":
    unittest.main()