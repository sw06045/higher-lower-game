import unittest
from src.card import Card, Deck
from src.shuffling.shuffle_strategies import DefaultShuffle

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card("Ace", "Spades")
        self.assertEqual(card.rank, "Ace")
        self.assertEqual(card.suit, "Spades")
        self.assertEqual(card.value, 50)

    def test_card_str(self):
        card = Card("Ace", "Spades")
        self.assertEqual(str(card), "Ace of Spades")

class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_creation_with_jokers(self):
        deck = Deck(include_jokers=True)
        self.assertEqual(len(deck.cards), 54)

    def test_deck_shuffle(self):
        deck = Deck()
        deck.set_shuffle_strategy(DefaultShuffle())
        original_order = deck.cards[:]
        deck.shuffle(seed=42)
        self.assertNotEqual(deck.cards, original_order)

    def test_deck_draw(self):
        deck = Deck()
        card = deck.draw()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)


if __name__ == "__main__":
    unittest.main()