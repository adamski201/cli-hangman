import console_interface
import driver


def main() -> None:
    renderer = console_interface.ConsoleInterface()

    game = driver.Driver()
    game.play_hangman()


if __name__ == '__main__':
    main()
