import logging
import sys

from PyQt6.QtWidgets import QApplication

from desktop.main_window import MainWindow

from finder.finder import ThresholdFinder
from fisherman import Fisherman
from gui_io.operator import Operator
from observer.observer import StandardObserver

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def run():

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    run()