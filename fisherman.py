from gui_io.operator import Operator


class Fisherman:

    def __init__(self, operator: Operator):
        self.operator = operator
        pass

    def fish(self):
        self.operator.window_manager.focus("World of Warcraft")
        self.operator.keyboard_manger.press_key("q")
        pass