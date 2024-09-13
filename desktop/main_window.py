import logging
import textwrap
from typing import Optional

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QPlainTextEdit, QLayout, QPushButton, \
    QLabel, QGridLayout

from desktop.fisherman_worker import FishermanWorker
from desktop.key_widget import KeyEdit
from desktop.logger_plain_text import LoggerPlainText, LoggerPlainTextLoggingHandler
from finder.finder import ThresholdFinder
from fisherman import Fisherman, logger
from gui_io.operator import Operator
from observer.observer import StandardObserver


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.worker: Optional[FishermanWorker] = None
        self.handler = LoggerPlainTextLoggingHandler()
        self.statistics = {}

        #  Pre-created widgets
        self.statistic_text = QLabel()
        self.reset_statistics_data()
        self.update_statistics()

        def validate_start_button_condition(key):
            self.update_start_button_status()

        self.cast_key_widget = KeyEdit()
        self.cast_key_widget.setKey("q") # TODO settings save/load
        self.cast_key_widget.signal_key.connect(validate_start_button_condition)

        self.start_button = QPushButton()
        self.start_button.setEnabled(False)

        self.setWindowTitle("Fisherman")
        self.setGeometry(100, 100, 400, 300)
        self.setMinimumSize(700, 400)

        # Create the main horizontal layout
        main_layout = QHBoxLayout()

        side_menu = self.create_side_menu()
        side_menu.setMaximumWidth(200)

        main_layout.addWidget(side_menu)
        main_layout.addWidget(self.create_logs_widget())

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget) #  don't get it why we can't use addLayout

        self.update_start_button_status()


    def create_logs_widget(self) -> QWidget:
        logs_text = LoggerPlainText()

        @pyqtSlot(str)
        def update_logs_text(message):
            logs_text.appendPlainText(message)

        self.handler.log_signal.connect(update_logs_text)

        if self.handler not in logging.getLogger().handlers:
            logging.getLogger().addHandler(self.handler)

        return logs_text

    def create_side_menu(self) -> QWidget:
        side_menu_widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,8,0)

        cast_key_label = QPushButton("Button 6")
        cast_key_label.setText("Cast")

        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Cast"), 0, 0)
        grid_layout.addWidget(self.cast_key_widget, 0, 1)

        layout.addLayout(grid_layout)

        layout.addStretch()

        self.start_button.setText("Start")
        self.start_button.clicked.connect(self.start_fishing)

        layout.addWidget(self.statistic_text)
        layout.addWidget(self.start_button)

        side_menu_widget.setLayout(layout)

        return side_menu_widget


    def start_fishing(self):

        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()

        operator = Operator.create(
            throw_key=self.cast_key_widget.key
        )

        fisherman = Fisherman(
            operator=operator,
            finder=ThresholdFinder(),
            observer=StandardObserver(operator)
        )

        self.reset_statistics_data()

        def handle_fishing_result(result):
            self.update_statistics_data(result)
            self.update_statistics()

        self.worker = FishermanWorker(fisherman)
        self.worker.update_signal.connect(handle_fishing_result)

        if not self.worker.isRunning():
            self.worker.start()

    def closeEvent(self, event): #  this is window close event

        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.disconnect()
            self.worker.wait(100)

            if self.worker.isRunning():
                self.worker.terminate()

        if self.handler:
            logging.getLogger().removeHandler(self.handler)
            self.handler.flush()
            self.handler.close()

        logging.shutdown()

        event.accept()

    def update_statistics_data(self, result):
        self.statistics["count"] = self.statistics["count"] + 1
        if result["success"]:
            self.statistics["successes"] = self.statistics["successes"] + 1
        else:
            self.statistics["fails"] = self.statistics["fails"] + 1

    def update_statistics(self):
        successes = 0
        fails = 0
        if self.statistics["count"] > 0:
            successes = (self.statistics["successes"]/self.statistics["count"]) * 100
            fails = (self.statistics["fails"]/self.statistics["count"]) * 100
        self.statistic_text.setText(textwrap.dedent(f"""
        Throws: {self.statistics["count"]}
        Successes: {successes:.0f}%
        Fails: {fails:.0f}%
        """))

    def reset_statistics_data(self):
        self.statistics = {
            "count": 0,
            "successes": 0,
            "fails": 0,
            "fails_to_find": 0,
            "fails_to_detect_movement": 0
        }

    def update_start_button_status(self):
        self.start_button.setEnabled(self.cast_key_widget.key is not None)