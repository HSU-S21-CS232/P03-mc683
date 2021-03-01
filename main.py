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

        ui_file.close()


        open_action = self.window.findChild(QAction, 'action_open')
        open_action.triggered.connect(self.open_action_triggered)

        quit_action = self.window.findChild(QAction, 'action_quit')
        quit_action.triggered.connect(self.quit_action_triggered)

        play_button = self.window.findChild(QPushButton, 'play_button')
        play_button.clicked.connect(self.play_button_clicked)

        self.window.show()

    def open_action_triggered(self):
        file_name = QFileDialog.getOpenFileName(self.window)
        self.music_player.setMedia(QUrl.fromLocalFile(file_name[0]))
