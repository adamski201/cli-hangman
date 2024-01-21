class Engine:
    def __init__(self, answer: str) -> None:
        self.answer: str = answer
        self.guessed: set[str] = set()
        self.mistakes: int = 0
        self.grid: list = [None] * len(answer)
        self.MAX_MISTAKES: int = 6

    def is_correct_guess(self, guess: str) -> bool:
        """Check if the guess appears in the answer."""
        return guess in self.answer

    def is_unique_guess(self, guess: str) -> bool:
        """Check if the guess has been guessed before in the current game."""
        return guess not in self.guessed

    def handle_guess(self, guess: str) -> bool:
        self.guessed.add(guess)

        if self.is_correct_guess(guess):
            self.update_grid(guess)

            return True
        else:
            self.mistakes += 1

            return False

    def update_grid(self, guess: str) -> None:
        """Update the grid by comparing the guess to the answer."""

        # Update in the case of an entire word guess
        if len(guess) > 1:
            if guess == self.answer:
                self.grid = list(self.answer)

        # Update in the case of a letter guess
        else:
            for idx, char in enumerate(self.answer):
                if char == guess:
                    self.grid[idx] = char

    def is_game_over(self) -> bool:
        """Check if the game is lost and return a bool."""
        return self.mistakes >= self.MAX_MISTAKES

    def is_game_won(self) -> bool:
        """Check if the game is won and return a bool."""
        return self.grid == list(self.answer)
