from fisherman import Fisherman
from io.window import WindowsWindowManager


def run():
    window_manager = WindowsWindowManager()
    fisherman = Fisherman(
        window_manager=window_manager
    )
    fisherman.fish()

if __name__ == '__main__':
    run()