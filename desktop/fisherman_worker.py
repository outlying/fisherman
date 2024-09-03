import time
from logging import getLogger

from PyQt6.QtCore import QThread, pyqtSignal

from fisherman import Fisherman


class FishermanWorker(QThread):

    update_signal = pyqtSignal(str)

    def __init__(self, fisherman: Fisherman):
        super().__init__()
        self._running = True
        self._fisherman = fisherman
        self.logger = getLogger(__name__)  # Get a logger for this class

    def run(self):
        while self._running:
            result = self._fisherman.fish()
            print(result)
            self.update_signal.emit("Running...")

    def stop(self):
        self._running = False