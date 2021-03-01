import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QFileDialog, QAction
from PySide2.QtCore import QFile, QObject, QUrl
from PySide2.QtMultimedia import QMediaPlayer

class MainWindow(QObject):
