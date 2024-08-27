from abc import ABC, abstractmethod
import pyautogui

class KeyboardManager(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def press_key(self, key):
        pass


class WindowsKeyboardManager(KeyboardManager):

    def __init__(self):
        super().__init__()

    def press_key(self, key):
        try:
            pyautogui.press(key)  # Simulate pressing the specified key
        except Exception as e:
            raise Exception(f"Error pressing key '{key}': {str(e)}")