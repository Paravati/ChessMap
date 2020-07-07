from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connectSignalsAndSlots()
        self.show()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow
        # self.ui.setupUi(self, MainWindow)  -> not working setup ui - need to be fixed

# pushButton_1, pushButton_2, pushButton_3, pushButton_4
    def connectSignalsAndSlots(self):
        pass

    def onClicked(self):
        pass


if __name__ == "__main__":
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys.excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        import sys

        print(sys.exc_info()[0])
        import traceback

        print(traceback.format_exc())
        import os

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)




