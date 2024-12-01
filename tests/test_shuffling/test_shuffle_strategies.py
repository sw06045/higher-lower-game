import unittest
from src.shuffling import shuffle_strategies
from src.card import Card

class TestShuffleStrategies(unittest.TestCase):
    def setUp(self):
        self.cards = [Card(rank, suit) for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] for suit in ["Clubs", "Diamonds", "Spades", "Hearts"]]

    def test_overhand_shuffle(self):
        strategy = shuffle_strategies.OverhandShuffle()
        shuffled_cards = strategy.shuffle(self.cards.copy(), seed=42)
        self.assertNotEqual(shuffled_cards, self.cards)

    def test_pile_shuffle(self):
        strategy = shuffle_strategies.PileShuffle()
        shuffled_cards = strategy.shuffle(self.cards.copy(), seed=42)
        self.assertNotEqual(shuffled_cards, self.cards)

    def test_pickup_shuffle(self):
        strategy = shuffle_strategies.PickupShuffle()
        shuffled_cards = strategy.shuffle(self.cards.copy(), seed=42)
        self.assertNotEqual(shuffled_cards, self.cards)

    def test_mongean_shuffle(self):
        strategy = shuffle_strategies.MongeanShuffle()
        shuffled_cards = strategy.shuffle(self.cards.copy(), seed=42)
        self.assertNotEqual(shuffled_cards, self.cards)

    def test_default_shuffle(self):
        strategy = shuffle_strategies.DefaultShuffle()
        shuffled_cards = strategy.shuffle(self.cards.copy(), seed=42)
        self.assertNotEqual(shuffled_cards, self.cards)

if __name__ == "__main__":
    unittest.main()