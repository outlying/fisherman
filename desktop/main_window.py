import logging
from typing import Optional

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QPlainTextEdit, QLayout, QPushButton

from desktop.fisherman_worker import FishermanWorker
from desktop.logger_plain_text import LoggerPlainText, LoggerPlainTextLoggingHandler
from finder.finder import ThresholdFinder
from fisherman import Fisherman
from gui_io.operator import Operator
from observer.observer import StandardObserver


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker: Optional[FishermanWorker] = None
        self.handler = LoggerPlainTextLoggingHandler()

        self.setWindowTitle("Fisherman")
        self.setGeometry(100, 100, 400, 300)
        self.setMinimumSize(700, 400)

        # Create the main horizontal layout
        main_layout = QHBoxLayout()

        main_layout.addLayout(self.create_side_menu())
        main_layout.addWidget(self.create_logs_widget())

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget) #  don't get it why we can't use addLayout


    def create_logs_widget(self) -> QWidget:
        logs_text = LoggerPlainText()

        @pyqtSlot(str)
        def update_logs_text(message):
            logs_text.appendPlainText(message)

        self.handler.log_signal.connect(update_logs_text)

        logging.getLogger().addHandler(self.handler)

        return logs_text

    def create_side_menu(self) -> QLayout:
        layout = QVBoxLayout()

        start_button = QPushButton()
        start_button.setText("Start")
        start_button.clicked.connect(self.start_fishing)

        layout.addWidget(start_button)

        return layout


    def start_fishing(self):

        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()

        operator = Operator.create()

        fisherman = Fisherman(
            operator=operator,
            finder=ThresholdFinder(),
            observer=StandardObserver(operator)
        )

        self.worker = FishermanWorker(fisherman)

        if not self.worker.isRunning():
            self.worker.start()

    def closeEvent(self, event): #  this is window close event

        if self.worker:
            self.worker.stop()
            self.worker.wait()
            event.accept()

        self.handler.log_signal.disconnect()
        logging.getLogger().removeHandler(self.handler)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)