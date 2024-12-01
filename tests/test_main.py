import unittest
from unittest.mock import patch
from src.main import main

class TestMain(unittest.TestCase):
    @patch("builtins.input", side_effect=["2", "0", "A", "B", "no", "exit()"])
    @patch("builtins.print")
    def test_main(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("\nWelcome to the Higher/Lower Game!")

if __name__ == "__main__":
    unittest.main()