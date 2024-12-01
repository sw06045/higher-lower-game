# Define the card deck
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
SUITS = ["Clubs", "Diamonds", "Spades", "Hearts"]

class Card:
    """Represents a playing card."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # Jokers have the highest value
        # Other cards are assigned values based on their rank and suit
        self.value = (RANKS.index(rank)) * 4 + SUITS.index(suit) if rank in RANKS else 52 

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Manages a deck of cards."""
    def __init__(self, include_jokers=False):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        if include_jokers:
            self.cards.extend([Card("Joker", "Black"), Card("Joker", "Red")])

    def set_shuffle_strategy(self, shuffle_strategy):
        self.shuffle_strategy = shuffle_strategy

    def shuffle(self, seed=None):
        self.cards = self.shuffle_strategy.shuffle(self.cards, seed)

    def draw(self):
        return self.cards.pop() if self.cards else None





