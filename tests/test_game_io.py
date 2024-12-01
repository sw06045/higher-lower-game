import unittest
from unittest.mock import patch
from src.game_io import GameIO
#from src.players.player import Player
from src.players.player_factory import PlayerFactory
import src.shuffling.shuffle_strategies as shuffle_strategies

class TestGameIO(unittest.TestCase):
    @patch("builtins.input", side_effect=["yes"])
    def test_prompt_include_jokers(self, mock_input):
        game_io = GameIO()
        result = game_io.prompt_include_jokers()
        self.assertTrue(result)

    @patch("builtins.input", side_effect=["2"])
    def test_prompt_num_players(self, mock_input):
        game_io = GameIO()
        result = game_io.prompt_num_players("human")
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["A", "B"])
    def test_prompt_human_player_names(self, mock_input):
        game_io = GameIO()
        result = game_io.prompt_human_player_names(2)
        self.assertEqual(result, ["A", "B"])

    @patch("builtins.input", side_effect=["easy", "medium"])
    def test_prompt_computer_player_names(self, mock_input):
        game_io = GameIO()
        result = game_io.prompt_computer_player_names(2)
        self.assertEqual(result, ["Computer 1 (easy)", "Computer 2 (medium)"])

    @patch("builtins.input", side_effect=["1"])
    def test_prompt_shuffle_strategy(self, mock_input):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            result = game_io.prompt_shuffle_strategy()
            mock_print.assert_called_with("4 -> Mongean Shuffle")
            self.assertIsInstance(result, shuffle_strategies.OverhandShuffle)

    @patch("builtins.input", side_effect=["yes"])
    def test_prompt_advanced_settings(self, mock_input):
        game_io = GameIO()
        result = game_io.prompt_advanced_settings()
        self.assertTrue(result)

    def test_display_welcome_message(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_welcome_message()
            mock_print.assert_called_with("\nWelcome to the Higher/Lower Game!")

    def test_display_starting_card(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_starting_card("Ace of Spades")
            mock_print.assert_any_call("Starting card:")
            mock_print.assert_any_call("\n\nAce of Spades\n\n")

    def test_display_next_card(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_next_card("Ace of Spades")
            mock_print.assert_any_call("\nNext card:")
            mock_print.assert_any_call("\n\nAce of Spades\n\n")

    def test_display_progress_bar(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_progress_bar(52, 26)
            mock_print.assert_called_with("\nDeck Progress: [####################--------------------] 26/52 cards remaining")

    def test_display_termination_message(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_termination_message()
            mock_print.assert_called_with("No more cards left in the deck.")

    def test_display_early_termination_message(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_early_termination_message()
            mock_print.assert_called_with("Game terminated early.")

    def test_display_current_scores(self):
        game_io = GameIO()
        players = [PlayerFactory.create_player("A"), PlayerFactory.create_player("B")]
        round_scores = ["+1", "-"]
        with patch("builtins.print") as mock_print:
            game_io.display_current_scores(players, round_scores)
            mock_print.assert_any_call("\n")
            mock_print.assert_any_call("A: 0 points|+1")
            mock_print.assert_any_call("B: 0 points|-")

    def test_display_final_scores(self):
        game_io = GameIO()
        players = [PlayerFactory.create_player("A"), PlayerFactory.create_player("B")]
        players[0].add_score(10)
        players[1].add_score(5)
        with patch("builtins.print") as mock_print:
            game_io.display_final_scores(players)
            mock_print.assert_any_call("Game over! Final scores")
            mock_print.assert_any_call("A: 10 points\nB: 5 points")

    def test_display_winner(self):
        game_io = GameIO()
        with patch("builtins.print") as mock_print:
            game_io.display_winner(["A"], 10)
            mock_print.assert_called_with("The winner is A with 10 points!")

if __name__ == "__main__":
    unittest.main()