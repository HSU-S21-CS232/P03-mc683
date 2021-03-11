import sys
from enum import Enum
from PySide2.QtUiTools import QUiLoader

from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox, QGridLayout, QSizePolicy
from PySide2.QtCore import QFile, QObject, QIODevice, Qt
from calcModel import Calculator


#I use examples and information from https://www.youtube.com/c/WandersonIsMe/featured . Very helpful and informative.

class ArithmeticOperations(Enum):
    Base = 0
    Add = '+'
    Subtract = '-'
    Multiply = '*'
    Divide = '/'

class MainWindow(QObject):
    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)

        self.calculator = Calculator()
        self.last_arithmetic_operation = ArithmeticOperations.Base

        #Load ui file to python.
        ui_file = QFile(ui_file)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open: {ui_file.errorString()}")
            sys.exit(-1)




        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        self.window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)


        #Be sure to close.
        ui_file.close()

        #Listeners for UI events.
        self.addEventListeners()

        #shows window.
        self.window.show()



    def addEventListeners(self):

        #add an event listener for press of buttons.
        self.window.findChild(QPushButton, 'button_zero').clicked.connect(self.zeroButtonClicked) #0
        self.window.findChild(QPushButton, 'button_one').clicked.connect(self.oneButtonClicked) #1
        self.window.findChild(QPushButton, 'button_two').clicked.connect(self.twoButtonClicked) #2
        self.window.findChild(QPushButton, 'button_three').clicked.connect(self.threeButtonClicked) #3
        self.window.findChild(QPushButton, 'button_four').clicked.connect(self.fourButtonClicked) #4
        self.window.findChild(QPushButton, 'button_five').clicked.connect(self.fiveButtonClicked) #5
        self.window.findChild(QPushButton, 'button_six').clicked.connect(self.sixButtonClicked) #6
        self.window.findChild(QPushButton, 'button_seven').clicked.connect(self.sevenButtonClicked) #7
        self.window.findChild(QPushButton, 'button_eight').clicked.connect(self.eightButtonClicked) #8
        self.window.findChild(QPushButton, 'button_nine').clicked.connect(self.nineButtonClicked) #9

        self.window.findChild(QPushButton, 'addition_button').clicked.connect(self.additionButtonClicked) #+
        self.window.findChild(QPushButton, 'subtract_button').clicked.connect(self.subtractButtonClicked) #-
        self.window.findChild(QPushButton, 'multiply_button').clicked.connect(self.multiplyButtonClicked) #*
        self.window.findChild(QPushButton, 'divide_button').clicked.connect(self.divideButtonClicked) #/

        self.window.findChild(QPushButton, 'clear_button').clicked.connect(self.clearButtonClicked)
        self.window.findChild(QPushButton, 'equals_button').clicked.connect(self.equalsButtonClicked)
        self.window.findChild(QPushButton, 'btn_close').clicked.connect(self.closebuttonclicked)

    def storeAccumulator(self):
        accumulator = self.window.findChild(QLineEdit, 'lineEdit')
        value = int(accumulator.text())
        self.calculator.load(value)
        accumulator.setText("")

    def doArithmetic(self):
        accumulator = self.window.findChild(QLineEdit, 'lineEdit')
        value = int(accumulator.text())
        if self.last_arithmetic_operation == ArithmeticOperations.Add:
            self.calculator.add(value)
        elif self.last_arithmetic_operation == ArithmeticOperations.Subtract:
            self.calculator.subtract(value)
        elif self.last_arithmetic_operation == ArithmeticOperations.Multiply:
            self.calculator.multiply(value)
        elif self.last_arithmetic_operation == ArithmeticOperations.Divide:
            self.calculator.divide(value)

        if self.last_arithmetic_operation != ArithmeticOperations.Base:
            accumulator.setText(str(self.calculator.value()))
            self.last_arithmetic_operation = ArithmeticOperations.Base

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
        accumulator.clear()


    def equalsButtonClicked(self, obj):
        self.doArithmetic()



    def additionButtonClicked(self, obj):
        self.doArithmetic()
        self.last_arithmetic_operation = ArithmeticOperations.Add
        self.storeAccumulator()

    def subtractButtonClicked(self, obj):
        self.doArithmetic()
        self.last_arithmetic_operation = ArithmeticOperations.Subtract
        self.storeAccumulator()

    def multiplyButtonClicked(self, obj):
        self.doArithmetic()
        self.last_arithmetic_operation = ArithmeticOperations.Multiply
        self.storeAccumulator()

    def divideButtonClicked(self, obj):
        self.doArithmetic()
        self.last_arithmetic_operation = ArithmeticOperations.Divide
        self.storeAccumulator()

    def closebuttonclicked(self, event):
        self.window.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('ui_main.ui')
    sys.exit(app.exec_())
