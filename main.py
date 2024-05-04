#!usr/bin/env python
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # loading set of letters
    tileset = tcod.tileset.load_tilesheet(
        "source.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

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
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)   # update screen

            # capture events
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()