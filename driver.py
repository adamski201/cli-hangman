import console_interface
import game as gm


class Driver:
    def __init__(self):
        self.game = gm.Game()

    def play_hangman(self) -> None:
        self.game.create_session()
        ui = console_interface.ConsoleInterface()

        while True:
            ui.display(self.game)

            if self.game.state == gm.State.MAIN_MENU:
                input()
                self.game.begin()

            elif self.game.state == gm.State.GAME_OVER:
                user_input = input().lower()
                if input == 'y':
                    self.game.create_session()
                    self.game.begin()
                else:
                    exit()

            elif self.game.state == gm.State.WAITING_FOR_INPUT:
                user_input = input()
                self.game.make_guess(user_input)

            elif self.game.state == gm.State.CORRECT_GUESS or self.game.state == gm.State.INCORRECT_GUESS:
                self.game.evaluate_win_or_lose()

            elif self.game.state == gm.State.GAME_WON or self.game.state == gm.State.GAME_LOST:
                self.game.end_game()

            else:
                self.game.reset_state_to_waiting()







