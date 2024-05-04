from typing import Tuple


class Entity:
    """
    a generic object to represent players, enemies, itmes, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx:int, dy:int) -> None:
        # move entity by given amount
        self.x += dx
        self.y += dy
