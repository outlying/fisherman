from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout


class KeyEdit(QLineEdit):

    signal_key = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(KeyEdit, self).__init__(*args, **kwargs)
        self.setFixedWidth(40)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setReadOnly(True)
        self.key = None

    def setKey(self, key):
        self.key = key
        self.setText(key)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.text().strip()

        if len(key) > 0:
            self.setKey(key)
            self.signal_key.emit(key)
        else:
            self.setKey(None)
            self.signal_key.emit(None)