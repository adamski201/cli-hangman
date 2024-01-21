from abc import ABC, abstractmethod

from game_state import GameState


class Renderer(ABC):
    @abstractmethod
    def display(self, game: GameState) -> None:
        pass
