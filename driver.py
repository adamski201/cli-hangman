import game_state
from game_state import State


class Driver:
    """
    Drive the progression of the game by informing the game_state of which state to move to,
    according to the current state and the user's input (if applicable).
    """

    def __init__(self, renderer):
        self.game = game_state.GameState()
        self.ui = renderer

    def is_valid_input(self, guess: str) -> bool:
        """Check if input is 1) a single character or 2) a word that matches the answer length."""
        return (
            len(guess) == 1
            or len(guess) == len(self.game.hangman.answer)
            and guess.isalpha()
        )

    def play_hangman(self) -> None:
        self.game.create_session()

        while True:
            self.ui.display(self.game)

            if self.game.state == State.MAIN_MENU:
                input()
                self.game.begin()

            elif self.game.state == State.GAME_OVER:
                user_input = input().lower()
                if user_input == "y":
                    self.game.create_session()
                    self.game.begin()
                else:
                    exit()

            elif self.game.state == State.WAITING_FOR_INPUT:
                user_input = input().lower()

                if self.is_valid_input(user_input):
                    self.game.make_guess(user_input)
                else:
                    self.game.set_invalid_input()

            elif (
                self.game.state == State.CORRECT_GUESS
                or self.game.state == State.INCORRECT_GUESS
            ):
                self.game.evaluate_win_or_lose()

            elif (
                self.game.state == State.GAME_WON or self.game.state == State.GAME_LOST
            ):
                self.game.end_game()

            else:
                self.game.reset_state_to_waiting()
