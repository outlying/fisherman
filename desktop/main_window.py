from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QPlainTextEdit, QLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fisherman")
        self.setGeometry(100, 100, 400, 300)
        # Set the minimum size for the window
        self.setMinimumSize(600, 400)

        # Create the main horizontal layout
        main_layout = QHBoxLayout()

        main_layout.addLayout(self.create_side_menu())
        main_layout.addWidget(self.create_logs_widget())

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget) #  don't get it why we can't use addLayout


    def create_logs_widget(self) -> QWidget:
        plain_text = QPlainTextEdit()
        plain_text.setReadOnly(True)
        return plain_text

    def create_side_menu(self) -> QLayout:
        layout = QVBoxLayout()

        start_button = QPushButton()
        start_button.setText("Start")

        layout.addWidget(start_button)

        return layout

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)