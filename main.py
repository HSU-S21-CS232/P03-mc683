import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QFileDialog, QAction
from PySide2.QtCore import QFile, QObject, QUrl
from PySide2.QtMultimedia import QMediaPlayer

class MainWindow(QObject):
    def __init__(self, ui_file, parent=none):

        self.music_player = QMediaPlayer()
        self.music_player.setVolume(100)

    super(MainWindow, self).__init__(parent)

    ui_file = QFile(ui_file)
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    self.window = loader.load(ui_file)    
