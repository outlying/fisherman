import logging

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPlainTextEdit


class LoggerPlainText(QPlainTextEdit):

    def __init__(self):
        super(LoggerPlainText, self).__init__()
        self.setReadOnly(True)

        font = QFont("Courier")
        font.setStyleHint(QFont.StyleHint.Monospace)

        self.setFont(font)

class LoggerPlainTextLoggingHandler(logging.Handler, QObject):
    log_signal = pyqtSignal(str)

    def __init__(self):
        logging.Handler.__init__(self)
        QObject.__init__(self)
        self.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    def emit(self, record):
        msg = self.format(record)
        self.log_signal.emit(msg)
