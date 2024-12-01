import shuffling.shuffle_strategies as shuffle_strategies

class GameIO:
    """Handles all input/output operations for the game."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameIO, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialise()
        return cls._instance

    def _initialise(self):
        pass


    def display_welcome_message(self):
        print("\nWelcome to the Higher/Lower Game!")
    
    def display_starting_card(self, current_card):
        print(f"Starting card:")
        self._display_card(current_card)
    
    def display_next_card(self, current_card):
        print(f"\nNext card:")
        self._display_card(current_card)
    
    def _display_card(self, current_card):
        print(f"\n\n{current_card}\n\n")

    def display_termination_message(self):
        print("No more cards left in the deck.")
    
    def display_early_termination_message(self):
        print("Game terminated early.")
    
    def display_current_scores(self, players, round_scores):
        print("\n")
        for player, round_score in zip(players, round_scores):
            print(f"{player}|{round_score}")

    def display_final_scores(self, players):
        scores = "\n".join(str(player) for player in players)
        print("Game over! Final scores")
        print(scores)

    def display_winner(self, winners, max_score):
        if len(winners) > 1:
            message = f"It's a tie between {', '.join(winners)} with {max_score} points!"
        else:
            message = f"The winner is {winners[0]} with {max_score} points!"
        print(message)

    def prompt_player_guess(self, player):
        guess = input(f"{player.name}, will the next card be Higher or Lower? ({player.higher_key}/{player.lower_key}): ").strip().lower()
        while guess not in [player.higher_key, player.lower_key]:
            if guess == "exit()":
                return "exit()"
            print(f"Invalid input. Please enter '{player.higher_key}' for Higher or '{player.lower_key}' for Lower.")
            guess = input(f"{player.name}, will the next card be Higher or Lower? ({player.higher_key}/{player.lower_key}): ").strip().lower()
        return guess
    
    def display_progress_bar(self, total_cards, remaining_cards):
        progress = (total_cards - remaining_cards) / total_cards
        bar_length = 40  # Length of the progress bar
        block = int(round(bar_length * progress))
        progress_bar = "#" * block + "-" * (bar_length - block)
        print(f"\nDeck Progress: [{progress_bar}] {remaining_cards}/{total_cards} cards remaining")


    def prompt_include_jokers(self):
        while True:
            include_jokers_input = input("Do you want to play with jokers? (yes/no): (default: no) ").strip().lower()
            if not include_jokers_input:
                return include_jokers_input == "no"
            if include_jokers_input in ["yes", "no"]:
                return include_jokers_input == "yes"
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def prompt_num_players(self, player_type):
        while True:
            try:
                num_players = int(input(f"Enter the number of {player_type} players: "))
                if player_type == "human" and num_players > 0:
                    return num_players
                elif player_type == "computer" and num_players >= 0:
                    return num_players
                else:
                    print(f"Number of {player_type} players cannot be negative or zero.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def prompt_human_player_names(self, num_human_players):
        player_names = []
        for i in range(num_human_players):
            name = input(f"Enter name for human player {i + 1}: (default: Player {i + 1}) ").strip()
            if not name:
                name = f"Player {i + 1}"
            player_names.append(name)
        return player_names

    def prompt_computer_player_names(self, num_computer_players):
        player_names = []
        for i in range(num_computer_players):
            difficulty = input(f"Enter difficulty for computer {i + 1} (easy, medium, hard): (default: medium) ").strip().lower()
            if not difficulty or difficulty not in ["easy", "medium", "hard"]:
                difficulty = "medium"
            player_names.append(f"Computer {i + 1} ({difficulty})")
        return player_names
    
    def prompt_shuffle_strategy(self):
        strategies = {
            "0": shuffle_strategies.DefaultShuffle(),
            "1": shuffle_strategies.OverhandShuffle(),
            "2": shuffle_strategies.PileShuffle(),
            "3": shuffle_strategies.PickupShuffle(),
            "4": shuffle_strategies.MongeanShuffle(),
        }
        print("\nSelect a shuffle strategy:")
        print("0 -> Default Shuffle")
        print("1 -> Overhand Shuffle")
        print("2 -> Pile Shuffle")
        print("3 -> Pickup Shuffle")
        print("4 -> Mongean Shuffle")
        
        choice = input("\nEnter the number of your choice: (default: 0 -> Default Shuffle) ").strip()
        return strategies.get(str(choice), shuffle_strategies.DefaultShuffle())
    

    def prompt_advanced_settings(self):
        while True:
            advanced_settings_input = input("Do you want to access advanced settings? (yes/no): (default: no) ").strip().lower()
            if not advanced_settings_input:
                return False
            if advanced_settings_input in ["yes", "no"]:
                return advanced_settings_input == "yes"
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")