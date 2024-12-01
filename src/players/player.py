from abc import ABC, abstractmethod
import random
from game_io import GameIO


class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.higher_key = "h"
        self.lower_key = "l"
        self.has_played = False
        self.game_io = GameIO()

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f"{self.name}: {self.score} points"

    @abstractmethod
    def play(self, current_card, deck):
        pass

# Potential for future features so use inheritance
class HumanPlayer(Player):
    """Represents a human player."""
    def play(self, current_card, deck):
        # Human player guess logic will be handled by GameIO
        return self.game_io.prompt_player_guess(self)

class DifficultyStrategy:
    """To encapsulates difficulty specific behavior for computer players."""
    def __init__(self, difficulty):
        self.accuracy = {"easy": 0.5, "medium": 0.75, "hard": 1.0}.get(difficulty, 0.75)

    def should_play_favorable(self):
        return random.random() < self.accuracy

class ComputerPlayer(Player):
    """Represents a computer controlled player."""
    def __init__(self, name="Computer", difficulty="medium"):
        super().__init__(name)
        self.strategy = DifficultyStrategy(difficulty.lower())
    
    def calculate_probabilities(self, current_card, deck):
        higher_count = sum(1 for card in deck.cards if card.value > current_card.value)
        lower_count = sum(1 for card in deck.cards if card.value < current_card.value)
        total_remaining = len(deck.cards)
        if total_remaining == 0:
            return 0.5, 0.5  # Default probabilities when no cards remain
        return higher_count / total_remaining, lower_count / total_remaining

    def play(self, current_card, deck):
        higher_prob, lower_prob = self.calculate_probabilities(current_card, deck)
        #print(f"Computer probabilities - Higher: {higher_prob:.2f}, Lower: {lower_prob:.2f}")

        favorable_choice = self.higher_key if higher_prob >= lower_prob else self.lower_key
        return favorable_choice if self.strategy.should_play_favorable() else (
            self.lower_key if favorable_choice == self.higher_key else self.higher_key
        )
