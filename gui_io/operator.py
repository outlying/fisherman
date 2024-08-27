import time

from gui_io.keyboard import KeyboardManager, WindowsKeyboardManager
from gui_io.screenshot import ScreenshotManager, WindowsScreenshotManager
from gui_io.window import WindowManager, WindowsWindowManager


class Operator:

    def __init__(self,
                 window_manager: WindowManager,
                 keyboard_manager: KeyboardManager,
                 screenshot_manager: ScreenshotManager,
                 throw_key: str = "q",
                 window_name: str = "World of Warcraft"):
        self.window_name = window_name
        self.window_manager = window_manager
        self.keyboard_manger = keyboard_manager
        self.screenshot = screenshot_manager
        pass

    def see(self):
        window = self.window_manager.focus(self.window_name)
        bbox = window.left, window.top, window.right, window.bottom
        time.sleep(0.5)
        return self.screenshot.take_screenshot(bbox)

    # noinspection PyMethodMayBeStatic
    def wait(self, amount_of_seconds):
        time.sleep(amount_of_seconds)

    def throw(self):
        self.keyboard_manger.press_key("q")
        pass

    @staticmethod
    def create():
        #  TODO do system selection here

        window_manager = WindowsWindowManager()
        keyword_manager = WindowsKeyboardManager()
        screenshot_manager = WindowsScreenshotManager()

        return Operator(
            window_manager=window_manager,
            keyboard_manager=keyword_manager,
            screenshot_manager=screenshot_manager
        )