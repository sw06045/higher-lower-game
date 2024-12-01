import unittest
from src.players.player_factory import PlayerFactory
from src.players.player import HumanPlayer, ComputerPlayer

class TestPlayerFactory(unittest.TestCase):
    def test_create_human_player(self):
        player = PlayerFactory.create_player("A")
        self.assertIsInstance(player, HumanPlayer)
        self.assertEqual(player.name, "A")

    def test_create_computer_player(self):
        player = PlayerFactory.create_player("Computer(easy)")
        self.assertIsInstance(player, ComputerPlayer)
        self.assertEqual(player.name, "Computer")
        self.assertEqual(player.strategy.accuracy, 0.5)

if __name__ == "__main__":
    unittest.main()