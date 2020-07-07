from PyQt5.QtWidgets import QMainWindow
from mainwindow import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connectSignalsAndSlots()
        self.show()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow

# pushButton_1, pushButton_2, pushButton_3, pushButton_4
    def connectSignalsAndSlots(self):
        pass

