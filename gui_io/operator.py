import time

from gui_io.keyboard import KeyboardManager, WindowsKeyboardManager
from gui_io.mouse import WindowsMouseManager, MouseManager
from gui_io.screenshot import ScreenshotManager, WindowsScreenshotManager
from gui_io.window import WindowManager, WindowsWindowManager


class Operator:

    def __init__(self,
                 window_manager: WindowManager,
                 keyboard_manager: KeyboardManager,
                 mouse_manager: MouseManager,
                 screenshot_manager: ScreenshotManager,
                 throw_key: str = "q",
                 window_name: str = "World of Warcraft"):
        self.window_name = window_name
        self.window_manager = window_manager
        self.keyboard_manger = keyboard_manager
        self.mouse_manager = mouse_manager
        self.screenshot = screenshot_manager
        self.throw_key = throw_key
        pass

    def move_away(self):
        self.mouse_manager.move(1, 1)

    def get_fish_at(self, x, y):
        window = self.window_manager.focus(self.window_name)
        self.mouse_manager.click(window.left + x, window.top + y)

    def abort_fishing(self):
        self.keyboard_manger.press_key("esc")
        self.wait(3)

    def see(self):
        window = self.window_manager.focus(self.window_name)
        bbox = window.left, window.top, window.right, window.bottom
        time.sleep(0.2)
        return self.screenshot.take_screenshot(bbox)

    def see_area(self, area):
        window = self.window_manager.focus(self.window_name)
        bbox = window.left + area[0], window.top + area[1], window.left + area[0] + area[2], window.top + area[1] + area[3]
        return self.screenshot.take_screenshot(bbox)

    # noinspection PyMethodMayBeStatic
    def wait(self, amount_of_seconds):
        time.sleep(amount_of_seconds)

    def throw(self):
        self.keyboard_manger.press_key(self.throw_key)
        pass

    @staticmethod
    def create():
        #  TODO do system selection here

        window_manager = WindowsWindowManager()
        keyword_manager = WindowsKeyboardManager()
        screenshot_manager = WindowsScreenshotManager()
        mouse_manager = WindowsMouseManager()

        return Operator(
            window_manager=window_manager,
            keyboard_manager=keyword_manager,
            mouse_manager=mouse_manager,
            screenshot_manager=screenshot_manager
        )