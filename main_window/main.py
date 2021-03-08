import sys
from PySide2.QtUiTools import QUiLoader

from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import QFile, QObject, QIODevice


#I use examples and information from https://www.youtube.com/c/WandersonIsMe/featured . Very helpful and informative.


class MainWindow(QObject):
    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)

        #Load ui file to python.
        ui_file = QFile(ui_file)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open: {ui_file.errorString()}")
            sys.exit(-1)


        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        #Be sure to close.
        ui_file.close()

        #Listeners for UI events.
        self.addEventListeners()

        #shows window.
        self.window.show()
