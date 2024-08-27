from io.window import WindowManager


class Fisherman:

    def __init__(self, window_manager: WindowManager):
        self.window_manager = window_manager
        pass

    def fish(self):
        self.window_manager.focus()
        pass