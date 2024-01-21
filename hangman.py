class Hangman:
    def __init__(self, answer: str) -> None:
        self.answer = answer
        self.guessed_letters = set()
        self.mistakes = 0
        self.grid = [None] * len(answer)
        self.MAX_MISTAKES = 6

    def is_correct_guess(self, guess: str) -> bool:
        return guess in self.answer

    def is_unique_guess(self, guess: str) -> bool:
        return guess not in self.guessed_letters

    def is_valid_letter_input(self, input: str) -> bool:
        return len(input) == 1 and input.isalpha()

    def handle_letter_guess(self, guess):
        self.guessed_letters.add(guess)

        if self.is_correct_guess(guess):
            self.update_grid(guess)

            return True
        else:
            self.mistakes += 1

            return False

    def update_grid(self, guess: str) -> None:
        for idx, char in enumerate(self.answer):
            if char == guess:
                self.grid[idx] = char

    def is_game_over(self) -> bool:
        return self.mistakes >= self.MAX_MISTAKES

    def is_game_won(self) -> bool:
        return self.grid == list(self.answer)
