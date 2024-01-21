import os
from game import State, Game


class ConsoleInterface:
    def __init__(self):
        self.rendered_hangman = [
            '''
            +---+
            |   |
                |
                |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            ''',
            '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            '''
        ]

    def clear_console(self) -> None:
        return os.system('clear')

    def render_hangman(self, mistakes) -> str:
        return self.rendered_hangman[mistakes]

    def render_grid(self, grid: list) -> str:
        new_grid = []
        for a in grid:
            if a:
                new_grid.append(a)
            else:
                new_grid.append("_")

        return "".join(new_grid)

    def display(self, game: Game) -> None:
        if game.state == State.MAIN_MENU:
            print("Welcome to Hangman!")
            print("Guess the word by entering a single character, or try to guess the entire word itself!")
            print("Press Enter when you are ready to begin.")

        elif game.state == State.WAITING_FOR_INPUT:
            self.clear_console()
            print(self.render_hangman(game.get_mistakes()))
            print("\n")
            print(f"Current attempt: {self.render_grid(game.get_grid())}")
            print("Enter a single character to make a guess: ")

        elif game.state == State.CORRECT_GUESS:
            print("You guessed correctly!")

        elif game.state == State.INCORRECT_GUESS:
            print("You guessed incorrectly...")

        elif game.state == State.GAME_WON:
            print("Well done, you've won!")

        elif game.state == State.GAME_LOST:
            print("You lose...")
            print(f"The correct word was {game.get_answer()}")

        elif game.state == State.INVALID_INPUT:
            print("Input not recognised. Please try again.")

        elif game.state == State.ALREADY_GUESSED:
            print("You have already guessed this character. Please try again.")

        elif game.state == State.GAME_OVER:
            print("Would you like to play again? (y/n): ")





