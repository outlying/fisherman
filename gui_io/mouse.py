from abc import ABC, abstractmethod
import pyautogui


class MouseManager(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def click(self, x, y, button='left'):
        """
        Perform a mouse click at the specified (x, y) coordinates with the specified button.
        :param x: The x-coordinate where the click should be performed.
        :param y: The y-coordinate where the click should be performed.
        :param button: The mouse button to click, 'left' or 'right'. Default is 'left'.
        """
        pass


class WindowsMouseManager(MouseManager):

    def __init__(self):
        super().__init__()

    def click(self, x, y, button='left'):
        """
        Perform a mouse click at the specified (x, y) coordinates with the specified button.
        :param x: The x-coordinate where the click should be performed.
        :param y: The y-coordinate where the click should be performed.
        :param button: The mouse button to click, 'left' or 'right'. Default is 'left'.
        """
        try:
            pyautogui.click(x=x, y=y, button=button)  # Simulate mouse click at (x, y) with specified button
        except Exception as e:
            raise Exception(f"Error clicking at ({x}, {y}) with button '{button}': {str(e)}")
