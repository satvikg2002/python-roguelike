#!usr/bin/env python
import tcod

def main() -> None:
    screen_width = 80
    screen_height = 50

    # loading set of letters
    tileset = tcod.tileset.load_tilesheet(
        "source.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

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
            root_console.print(x=10, y=10, string="@")

            context.present(root_console)   # update screen

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()