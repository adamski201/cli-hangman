import os
import time
from game_state import State, GameState
from renderer import Renderer


class ConsoleInterface(Renderer):
    def clear_console(self) -> None:
        os.system("clear")

    def render_hangman(self, mistakes) -> str:
        return rendered_hangman[mistakes]

    def render_grid(self, grid: list) -> str:
        new_grid = []
        for a in grid:
            if a:
                new_grid.append(a)
            else:
                new_grid.append("_")

        return "".join(new_grid)

    def render_already_guessed(self, guessed: set):
        return ",".join(sorted(list(guessed)))

    def print_current_status(self, game: GameState) -> None:
        self.clear_console()
        print(f"You've guessed: {self.render_already_guessed(game.hangman.guessed)}")
        print(self.render_hangman(game.hangman.mistakes))
        print(f"Current attempt: {self.render_grid(game.hangman.grid)}")

    def display(self, game: GameState) -> None:
        if game.state == State.MAIN_MENU:
            self.clear_console()
            print("Welcome to Hangman!")
            print(
                "Guess the word by entering a single character, or try to guess the entire word itself!"
            )
            print("Press Enter when you are ready to begin.")

        elif game.state == State.WAITING_FOR_INPUT:
            self.print_current_status(game)

            print("Make a guess: ")

        elif game.state == State.CORRECT_GUESS:
            print("You guessed correctly!")
            time.sleep(1.5)

        elif game.state == State.INCORRECT_GUESS:
            print("You guessed incorrectly...")
            time.sleep(1.5)

        elif game.state == State.GAME_WON:
            self.print_current_status(game)
            time.sleep(1)
            print("Well done, you've won!")

        elif game.state == State.GAME_LOST:
            self.print_current_status(game)
            time.sleep(1)
            print("You lose...")
            print(f"The correct word was {game.hangman.answer}.")

        elif game.state == State.INVALID_INPUT:
            print("Input not recognised. Please try again.")
            time.sleep(1)

        elif game.state == State.ALREADY_GUESSED:
            print("You have already guessed this character. Please try again.")
            time.sleep(1.5)

        elif game.state == State.GAME_OVER:
            time.sleep(1.5)
            print("Would you like to play again? (y/n): ")


rendered_hangman = [
    """
            +---+
            |   |
                |
                |
                |
                |
            =========
            """,
    """
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            """,
    """
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            """,
    """
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            """,
    """
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            """,
    """
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            """,
    """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            """,
]
