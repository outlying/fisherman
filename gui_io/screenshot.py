from abc import ABC, abstractmethod
from PIL import ImageGrab

class ScreenshotManager(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def take_screenshot(self, x: int, y: int, width: int, height: int):
        pass


class WindowsScreenshotManager(ScreenshotManager):

    def __init__(self):
        super().__init__()

    def take_screenshot(self, x: int, y: int, width: int, height: int):
        try:
            # Define the bounding box (left, upper, right, lower)
            bbox = (x, y, x + width, y + height)
            # Capture the portion of the screen defined by bbox
            screenshot = ImageGrab.grab(bbox=bbox)
            return screenshot
        except Exception as e:
            raise Exception(f"Error taking screenshot: {str(e)}")