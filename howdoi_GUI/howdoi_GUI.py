from PySide2.QtCore import Signal
from PySide2.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QWidget, QLabel, QLineEdit, QVBoxLayout)
import sys

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        with open('.\styleSheets\window.qss','r') as stylesheet:
            self._style = stylesheet.read()
        self.setStyleSheet(self._style)
            
        self.container= QWidget(self)
        self.label= QLabel(self.container)
        
        self.input= QLineEdit(self.container)
        self.input.textChanged.connect(self.label.setText)
        
        self.button= QPushButton("Push me",self.container)
        self.button.clicked.connect(self.button_clicked)
        self.button.released.connect(self.button_released)
        
        
        layout= QVBoxLayout(self.container)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)
        
        
        
    def button_clicked(self):
        self.button.setStyleSheet()
        
    def button_released(self):
        self.button.clearFocus()



if __name__ == '__main__':
    app= QApplication(sys.argv)
    window= MainWindow("Howdoi")
    window.show()
    app.exec_()