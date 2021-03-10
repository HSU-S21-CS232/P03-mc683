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

        #add an event listener for press of buttons.
        zeroButton = self.window.findChild(QPushButton, 'button_zero')
        zeroButton.clicked.connect(self.zeroButtonClicked)
        oneButton = self.window.findChild(QPushButton, 'button_one')
        oneButton.clicked.connect(self.oneButtonClicked)
        twoButton = self.window.findChild(QPushButton, 'button_two')
        twoButton.clicked.connect(self.twoButtonClicked)
        threeButton = self.window.findChild(QPushButton, 'button_three')
        threeButton.clicked.connect(self.threeButtonClicked)
        fourButton = self.window.findChild(QPushButton, 'button_four')
        fourButton.clicked.connect(self.fourButtonClicked)
        fiveButton = self.window.findChild(QPushButton, 'button_five')
        fiveButton.clicked.connect(self.fiveButtonClicked)
        sixButton = self.window.findChild(QPushButton, 'button_six')
        sixButton.clicked.connect(self.sixButtonClicked)
        sevenButton = self.window.findChild(QPushButton, 'button_seven')
        sevenButton.clicked.connect(self.sevenButtonClicked)
        eightButton = self.window.findChild(QPushButton, 'button_eight')
        eightButton.clicked.connect(self.eightButtonClicked)
        nineButton = self.window.findChild(QPushButton, 'button_nine')
        nineButton.clicked.connect(self.nineButtonClicked)

        additionButton = self.window.findChild(QPushButton, 'addition_button')
        additionButton.clicked.connect(self.additionButtonClicked)
        subtractButton = self.window.findChild(QPushButton, 'subtract_button')
        subtractButton.clicked.connect(self.subtractButtonClicked)
        multiplyButton = self.window.findChild(QPushButton, 'multiply_button')
        multiplyButton.clicked.connect(self.multiplyButtonClicked)
        divideButton = self.window.findChild(QPushButton, 'divide_button')
        divideButton.clicked.connect(self.divideButtonClicked)

        clearButton = self.window.findChild(QPushButton, 'clear_button')
        clearButton.clicked.connect(self.clearButtonClicked)

    def zeroButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_zero')
        self.handlButtonClick(button)

    def oneButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_one')
        self.handlButtonClick(button)

    def twoButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_two')
        self.handlButtonClick(button)

    def threeButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_three')
        self.handlButtonClick(button)

    def fourButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_four')
        self.handlButtonClick(button)

    def fiveButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_five')
        self.handlButtonClick(button)

    def sixButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_six')
        self.handlButtonClick(button)

    def sevenButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_seven')
        self.handlButtonClick(button)

    def eightButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_eight')
        self.handlButtonClick(button)

    def nineButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'button_nine')
        self.handlButtonClick(button)

    def handlButtonClick(self, button):
        accumulator = self.window.findChild(QLineEdit, 'lineEdit')
        new_text = accumulator.text() + button.text()
        accumulator.setText(new_text)

    def clearButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'clear_button')
        accumulator = self.window.findChild(QLineEdit, 'lineEdit')
        accumulator.setText('')

    def additionButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'addition_button')
        self.handlButtonClick(button)

    def subtractButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'subtract_button')
        self.handlButtonClick(button)

    def multiplyButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'multiply_button')
        self.handlButtonClick(button)

    def divideButtonClicked(self, obj):
        button = self.window.findChild(QPushButton, 'divide_button')
        self.handlButtonClick(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('ui_main.ui')
    sys.exit(app.exec_())
