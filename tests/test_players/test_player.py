import unittest
from unittest.mock import patch
from src.players.player import Player, HumanPlayer, ComputerPlayer, DifficultyStrategy
from src.players.player_factory import PlayerFactory
from src.card import Card, Deck

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = PlayerFactory.create_player("A")
        self.assertEqual(player.name, "A")
        self.assertEqual(player.score, 0)
        self.assertEqual(player.higher_key, "h")
        self.assertEqual(player.lower_key, "l")

    def test_add_score(self):
        player = PlayerFactory.create_player("A")
        player.add_score(10)
        self.assertEqual(player.score, 10)

class TestHumanPlayer(unittest.TestCase):
    def test_human_player_creation(self):
        player = HumanPlayer("A")
        self.assertEqual(player.name, "A")
        self.assertEqual(player.score, 0)

class TestComputerPlayer(unittest.TestCase):
    def test_computer_player_creation(self):
        computer_player = ComputerPlayer("Computer", "easy")
        self.assertEqual(computer_player.name, "Computer")
        self.assertEqual(computer_player.strategy.accuracy, 0.5)
    
    def test_calculate_probabilities(self):
        computer_player = ComputerPlayer("Computer", "easy")
        deck = Deck()
        current_card = deck.draw()
        higher_prob, lower_prob = computer_player.calculate_probabilities(current_card, deck)
        self.assertEqual(higher_prob, 0.0)
        self.assertEqual(lower_prob, 1.0)

    def test_make_guess(self):
        computer_player = ComputerPlayer("Computer", "medium")
        deck = Deck()
        current_card = Card("7", "Hearts")
        with patch("builtins.print") as mock_print:
            guess = computer_player.play(current_card, deck)
            mock_print.assert_any_call("Computer probabilities - Higher: 0.54, Lower: 0.44")
            self.assertIn(guess, [computer_player.higher_key, computer_player.lower_key])
        

class TestDifficultyStrategy(unittest.TestCase):
    def test_difficulty_strategy(self):
        strategy = DifficultyStrategy("hard")
        self.assertEqual(strategy.accuracy, 1.0)
        strategy = DifficultyStrategy("unknown")
        self.assertEqual(strategy.accuracy, 0.75)

if __name__ == "__main__":
    unittest.main()