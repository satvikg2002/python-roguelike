#!usr/bin/env python
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    # loading set of letters
    tileset = tcod.tileset.load_tilesheet(
        "source.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    # set up terminal
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Python Roguelike",
        vsync=True
    ) as context:
        
        root_console = tcod.console.Console(screen_width, screen_width, order="F")

        # game loop
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            events = tcod.event.wait()


if __name__ == "__main__":
    main()