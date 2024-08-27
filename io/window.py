from abc import ABC, abstractmethod

class WindowManager(ABC):

    def __init__(self):
        pass

    def focus(self):
        pass


class WindowsWindowManager(WindowManager):

    def __init__(self):
        super().__init__()

    def focus(self):
        pass