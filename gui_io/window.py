from abc import ABC, abstractmethod
import pygetwindow as gw


class WindowManager(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_window(self, window_name: str):
        pass


class WindowsWindowManager(WindowManager):

    def __init__(self):
        super().__init__()

    def get_window(self, window_name: str):
        # Get the list of all open windows
        windows = gw.getWindowsWithTitle(window_name)
        if not windows:
            raise Exception(f"No window with title '{window_name}' found.")

        # Assuming we focus on the first matching window
        window = windows[0]
        return window