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


    def addEventListeners(self):

        #add an event listener for press of the 7 button
        sevenButton = self.window.findChild(QPushButton, 'button_seven')
        sevenButton.clicked.connect(self.sevenButtonClicked)
        eightButton = self.window.findChild(QPushButton, 'button_eight')
        eightButton.clicked.connect(self.eightButtonClicked)

    def sevenButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_seven')
        self.handlButtonClick(button)

    def eightButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_eight')
        self.handlButtonClick(button)

    def handlButtonClick(self, button):
        accumulator = self.window.findChild(QLineEdit, 'lineEdit')
        new_text = accumulator.text() + button.text()
        accumulator.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('ui_main.ui')
    sys.exit(app.exec_())
