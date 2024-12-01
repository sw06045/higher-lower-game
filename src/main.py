from higher_lower_game import HigherLowerGame
import shuffling.shuffle_strategies as shuffle_strategies
from game_io import GameIO

def main():
    game_io = GameIO()
    game_io.display_welcome_message()
    
    num_human_players = game_io.prompt_num_players("human")
    num_computer_players = game_io.prompt_num_players("computer")

    player_names = game_io.prompt_human_player_names(num_human_players)
    player_names += game_io.prompt_computer_player_names(num_computer_players)
    
    # Default hard coded inputs
    include_jokers = False
    shuffle_strategy = shuffle_strategies.DefaultShuffle()
    
    if game_io.prompt_advanced_settings():
        shuffle_strategy = game_io.prompt_shuffle_strategy()
        include_jokers = game_io.prompt_include_jokers()

    game = HigherLowerGame(player_names, include_jokers)
    game.deck.set_shuffle_strategy(shuffle_strategy)
    game.start_game()

if __name__ == "__main__":
    main()
