from typing import Tuple

from game_map import GameMap
import tile_types

class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x             # top left corner
        self.y1 = y             # top left corner
        self.x2 = x + width     # bottom right corner
        self.y2 = y + height    # bottom right corner

    @property   # read-only variable for the class
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y
    
    @property
    def inner(self) -> Tuple[slice, slice]:
        """ Return the inner area of this room as a 2D array index. """
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)     # +1 to ensure wall
    

def generate_dungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor

    return dungeon