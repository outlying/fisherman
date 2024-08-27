from abc import ABC, abstractmethod

from gui_io.operator import Operator


class Observer(ABC):

    @abstractmethod
    def observe(self, area):
        pass

class StandardObserver(Observer):

    def __init__(self, operator: Operator):
        self.operator = operator

    def observe(self, area):
        while True:
            pass
        pass