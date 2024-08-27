from abc import ABC, abstractmethod
from PIL import ImageGrab

class ScreenshotManager(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def take_screenshot(self, bbox):
        pass


class WindowsScreenshotManager(ScreenshotManager):

    def __init__(self):
        super().__init__()

    def take_screenshot(self, bbox):
        try:
            screenshot = ImageGrab.grab(bbox=bbox)
            return screenshot
        except Exception as e:
            raise Exception(f"Error taking screenshot: {str(e)}")