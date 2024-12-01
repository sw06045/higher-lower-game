from card import Deck
from players.player_factory import PlayerFactory
from game_io import GameIO

class HigherLowerGame:
    """Manages the Higher/Lower game."""
    def __init__(self, player_names, include_jokers):
        self.players = [PlayerFactory.create_player(name) for name in player_names]
        self.deck = Deck(include_jokers)
        self.current_card = None
        self.game_io = GameIO()
        self.total_cards = len(self.deck.cards)


    def start_game(self):
        self.deck.shuffle()
        self.current_card = self.deck.draw()
        self.game_io.display_starting_card(self.current_card)
        

        while self.deck.cards:
            round_scores = []
            next_card = self.deck.draw()
            for player in self.players:

                guess = player.play(self.current_card, self.deck)
                if guess == "exit()":
                    self.game_io.display_early_termination_message()
                    self.display_winner()
                    return
                
                awarded = self.process_guess(player, guess, next_card)

                round_scores.append("+1" if awarded else "-")
            
            self.game_io.display_current_scores(self.players, round_scores)

            self.current_card = next_card
            self.game_io.display_progress_bar(self.total_cards, len(self.deck.cards))
            self.game_io.display_next_card(self.current_card)
            
        
        self.game_io.display_termination_message()
        
        self.display_winner()


    def process_guess(self, player, guess, next_card):
        if self.evaluate_guess(guess, next_card):
            player.add_score(1)
            return True
        else:
            return False

    def evaluate_guess(self, guess, next_card):
        # Single case when two consecutive Jokers are drawn
        if next_card.value == self.current_card.value:
            return True
        if guess == "h" and next_card.value > self.current_card.value:
            return True
        if guess == "l" and next_card.value < self.current_card.value:
            return True
        return False

    def display_winner(self):
        self.game_io.display_final_scores(self.players)
        max_score = max(player.score for player in self.players)
        winners = [player.name for player in self.players if player.score == max_score]
        self.game_io.display_winner(winners, max_score)