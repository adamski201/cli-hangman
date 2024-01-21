import hangman as hm
import random
import csv
from enum import Enum


class State(Enum):
    MAIN_MENU = 0
    WAITING_FOR_INPUT = 1
    CORRECT_GUESS = 2
    INCORRECT_GUESS = 3
    INVALID_INPUT = 4
    ALREADY_GUESSED = 5
    GAME_WON = 6
    GAME_LOST = 7
    GAME_OVER = 8


class Game:
    def __init__(self):
        self.hangman = None
        self.state = None

    @staticmethod
    def get_random_word_from_dictionary() -> str:
        try:
            with open("words.txt", newline="") as words:
                reader = csv.reader(words)

                word_list = list(reader)[0]

                return random.choice(word_list)

        except FileNotFoundError:
            raise Exception(
                "Words.txt not found. Ensure it is in the same directory as this file.")

    def create_session(self) -> None:
        self.hangman = hm.Hangman(self.get_random_word_from_dictionary())
        self.state = State.MAIN_MENU

    def begin(self) -> None:
        self.state = State.WAITING_FOR_INPUT

    def make_guess(self, guess) -> None:
        if not self.hangman.is_valid_letter_input(guess):
            self.state = State.INVALID_INPUT
            return

        if not self.hangman.is_unique_guess(guess):
            self.state = State.ALREADY_GUESSED
            return

        if self.hangman.handle_letter_guess(guess):
            self.state = State.CORRECT_GUESS
        else:
            self.state = State.INCORRECT_GUESS

    def evaluate_win_or_lose(self) -> None:
        if self.hangman.is_game_won():
            self.state = State.GAME_WON
        elif self.hangman.is_game_over():
            self.state = State.GAME_LOST
        else:
            self.state = State.WAITING_FOR_INPUT

    def reset_state_to_waiting(self) -> None:
        self.state = State.WAITING_FOR_INPUT

    def end_game(self) -> None:
        self.state = State.GAME_OVER

    def get_mistakes(self) -> int:
        return self.hangman.mistakes

    def get_grid(self) -> list:
        return self.hangman.grid

    def get_answer(self) -> str:
        return self.hangman.answer
