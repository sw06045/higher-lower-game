# Higher-Lower Game
This project implements a Higher/Lower card game where players guess whether the next card drawn from the deck will be higher or lower than the current card. The game supports both human and computer players, and various shuffling algorithms can be used to shuffle the deck.

# Content
[Usage](#usage)

[Source Code Documentation](#source-code-documentation)

[Future Improvements](#future-improvements)

# Usage
To start the application, run the `main.py` file:
```bash
python main.py
```

All instructions will be provided via the command line interface (CLI) once the game starts. To exit the game early once the game starts, type:
```python
exit()
```



# Source Code Documentation

## main.py
The main.py file serves as the entry point for the Higher/Lower card game application. It initialises the game, prompts the user for necessary inputs, sets up the game configuration, and starts the game.

## game_io.py
The game_io.py file defines the GameIO class, which handles all input/output operations for the Higher/Lower game. The class uses the singleton pattern to ensure a single point of control for user interactions. The display methods provide clear feedback to the user, while the prompt methods handle user input with validation and default values.
#### Design Decisions
- **Input Validation**:
    - Ensure that the user provides valid inputs.
    - Example: `prompt_player_guess` ensures the user enters either the higher or lower key.
- **Simplify User Experience**:
    - Some prompt methods provide default values.
    - Example: `prompt_include_jokers` defaults to "no" if the user does not provide an input.
- **Avoid Code Duplication**:
    - `_display_card` method is used by both `display_starting_card` and `display_next_card`.
    - Ensures consistency in how cards are displayed.
- **Easily Extend for GUI**:
    - Keeping the a centralised interface with the user allows for easier extension for GUI in future development

## higher_lower_game.py
The `start_game` method manages the main game loop, handling the shuffling of the deck, drawing cards, processing player guesses, and updating the game state.
**Steps**:
1. **Shuffle the Deck**: The deck is shuffled using the specified shuffle strategy.
2. **Draw the Starting Card**: The first card is drawn from the deck and displayed as the starting card.
3. **Main Game Loop**: The game continues as long as there are cards in the deck.
4. **Round Scores**: A list to keep track of the scores for the current round.
5. **Draw the Next Card**: The next card is drawn from the deck.
6. **Player Guesses**: Each player makes a guess (higher or lower) based on the current card.
7. **Early Termination**: If a player chooses to exit, the game displays an early termination message and the winner.
8. **Process Guesses**: The guesses are processed, and scores are updated.
9. **Update Display**: The current scores, progress bar, and next card are displayed.
#### Design Decisions
- **Game Loop**: 
	- The main game loop ensures that the game continues until there are no more cards left in the deck. This loop handles player interactions and updates the game state after each round.
- **Early Termination**: 
	- The option for players to exit the game early is provided, allowing for flexibility in game duration and accommodating player preferences.
- **Display Updates**: 
	- The game state is continuously updated and displayed to the players, providing clear feedback and enhancing the user experience.
- **Multiple Winners**: 
	- The method accounts for the possibility of multiple winners, ensuring that ties are handled correctly.

## player.py
The `player.py` file defines the classes and logic related to players in the Higher/Lower game. The `Player` class serves as an abstract base class for both human and computer players, providing common functionality. The `HumanPlayer` class represents a human player and interacts with the user through the `GameIO` instance. The `DifficultyStrategy` class encapsulates the behavior of computer players based on the difficulty level, and the `ComputerPlayer` class represents a computer-controlled player, using probabilities and strategy to make decisions.
#### Design Decisions:
- **Inheritance**: 
	- The `HumanPlayer` class inherits from the `Player` class, allowing it to use the common functionality defined in the base class.
- **Difficulty Levels**: 
	- The class supports three difficulty levels: easy, medium, and hard. Each level has a different accuracy, allowing for varying levels of challenge.
- **Randomness**: 
	- The `should_play_favorable` method uses the `random` module to determine whether the computer player should make a favorable guess, introducing an element of randomness.
- **Probability Calculation**: 
	- The `calculate_probabilities` method in the `ComputerPlayer` class determines the likelihood of the next card being higher or lower than the current card. This calculation is based on the remaining cards in the deck and their values.
##### Algorithm to Calculate Probabilities
1. **Identify Remaining Cards**: Determine the cards that are still in the deck.
2. **Count Higher and Lower Cards**: Count the number of cards that are higher and lower than the current card.
3. **Calculate Probabilities**: Use the counts to calculate the probabilities of the next card being higher or lower.

Let:

- $\( V_C \)$ be the value of the current card.
- $\( N \)$ be the total number of remaining cards in the deck.
- $\( H \)$ be the number of cards in the deck with a value higher than $\( V_C \)$.
- $\( L \)$ be the number of cards in the deck with a value lower than $\( V_C \)$.

The probability $\( P_H \)$ of the next card being higher than the current card is given by:

$\[ P_H = \frac{H}{N} \]$

The probability $\( P_L \)$ of the next card being lower than the current card is given by:

$\[ P_L = \frac{L}{N} \]$

## player_factory.py
The `player_factory.py` file defines the `PlayerFactory` class, which provides a static method for creating instances of `HumanPlayer` and `ComputerPlayer` based on the provided name.
#### Design Decisions:
- **Factory Pattern**: The use of the factory pattern allows for the encapsulation of player creation logic in a single place. This makes the code more modular and easier to maintain, as changes to the player creation logic only need to be made in one place.
- **Flexibility**: The factory method provides flexibility in creating different types of players based on the provided name. This makes it easy to add new types of players or modify the player creation logic in the future.

## card.py
The card.py file defines the fundamental components of a deck of playing cards, including individual cards (Card class) and the deck itself (Deck class). 
#### Design Decisions
- **Suit Order**: 
	- Suits are ranked alphabetically: clubs, diamonds, hearts, and spades. 
- **Value Calculation**:
    - The value of a card is determined by its rank's index in the `RANKS` list and its suit's index in the `SUITS` list.
    - This ensures each card has a unique value, useful for comparing cards.
- **Jokers**:
    - Assigned a special value of 52, higher than any other card.
    - Simplifies the logic for handling Jokers in the game.
- **Shuffle Strategy**:
	- The Deck class uses a strategy pattern for shuffling.
	- This allows different shuffling algorithms to be used interchangeably.
	- The `set_shuffle_strategy` method sets the shuffle strategy, and the `shuffle` method uses this strategy to shuffle the deck.

## shuffle_algorithms.py
The `shuffle_algorithms.py` file defines various shuffling algorithms that can be used to shuffle a list of items. Each algorithm provides a different method for randomising the order of the items, ensuring a thorough and effective shuffle. Inspired by shuffling techniques found [here](https://en.wikipedia.org/wiki/Shuffling).
- overhand
	- **Process**:
		- **Initialisation**: The function initialises the length of the list and creates an empty list (`shuffled_list`) of the same length.
		- **Shuffling Loop**: The function iterates through the original list, taking a small number of items (between 1 and 5) and placing them into the shuffled list in reverse order.
		- **Recursion**: The function recursively shuffles the list the specified number of times.
- pile
	- **Process**:
        - **Dividing into Piles**: The list is divided into a number of piles.
        - **Combining Piles**: The piles are combined in a random order to form the shuffled list.
        - **Repetition**: The process is repeated the specified number of times.
- 52_pickup
	- **Process**:
		- **Picking up**: Random cards are picked randomly from the deck one at a time.
		- **Repetition**: The process is repeated the specified number of times.
- mongean
	- **Process**:
		- **Alternating Placement**: Items are alternately placed at the front and back of the shuffled list.
		- **Repetition**: The process is repeated the specified number of times.
- DefaultShuffle
	- Uses the default shuffle algorithm (`random.shuffle`).

## shuffle_strategies.py
The shuffle_strategies.py file defines various shuffling strategies that inherits different shuffling algorithms. The file uses the strategy pattern to allow for interchangeable shuffling strategies, providing flexibility in how the deck of cards is shuffled. Each strategy class implements the shuffle method, adhering to the common interface defined by the ShuffleStrategy abstract base class.


# Future Improvements
1. **Modularise the Codebase**
    - **Action**: Break down large files into smaller, more focused modules. For example, separate the `game_io.py` file into multiple files such as `input_handler.py`, `output_handler.py`, and `prompt_handler.py`.
    - **Why**: This will make the codebase easier to navigate and maintain. Each module will have a single responsibility, adhering to the Single Responsibility Principle. 
2. **Implement a Graphical User Interface (GUI)**
    - **Action**: Develop a GUI using a framework like Tkinter, PyQt. This will involve creating windows, buttons, and other interactive elements to replace the command line interface.
    - **Why**: A GUI will enhance the user experience by making the game more visually appealing and easier to interact with. It will also be a good technical challenge to learn and implement GUI programming.
3. **Add Network Multiplayer Support**
    - **Action**: Implement network multiplayer functionality using sockets or a library like `socketio` or `websockets`. This will involve setting up a server to manage game state and client connections for each player.
    - **Why**: It will also provide a challenging opportunity to work with networking and concurrency.
4. **Implement a Detailed Statistics and Leaderboard System**
	- **Action**: Develop a system to track and display detailed statistics for each player, such as win/loss records, average scores, and highest scores. Additionally, create a leaderboard to rank players based on their performance.
	- **Why**: This feature will add a competitive element to the game, encouraging players to improve their performance and compare their results with others. It will also be a good technical challenge to design and implement a persistent data storage solution, such as using a database or file system, to keep track of player statistics and leaderboard information.
