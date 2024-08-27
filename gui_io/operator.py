from abc import ABC, abstractmethod

from gui_io.keyboard import KeyboardManager, WindowsKeyboardManager
from gui_io.window import WindowManager, WindowsWindowManager


class Operator(ABC):

    def __init__(self,
                 window_manager: WindowManager,
                 keyboard_manager: KeyboardManager):
        self.window_manager = window_manager
        self.keyboard_manger = keyboard_manager
        pass

    @staticmethod
    def create():
        #  TODO do system selection here

        window_manager = WindowsWindowManager()
        keyword_manager = WindowsKeyboardManager()

        return Operator(
            window_manager=window_manager,
            keyboard_manager=keyword_manager
        )