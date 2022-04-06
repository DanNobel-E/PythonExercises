from PySide2.QtCore import Signal
from howdoAIV_howdoi_parser import HowdoAIV_Parser
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QMenuBar)
import sys

class HowdoAIV_MainWindow(QMainWindow):
    def __init__(self, title, width, height):
        super().__init__()
        #main window settings
        self.setWindowTitle(title)
        self.width= width
        self.height =height
        self.setFixedSize(width,height)
        self.howdoi_parser= HowdoAIV_Parser()
        
        #stylesheet management 
        with open('..\styleSheets\window.qss','r') as stylesheet:
            self._style = stylesheet.read()
        self.setStyleSheet(self._style)
        
        #layouts dictionary
        self.layouts= {}
        
        #header
        header = QWidget(self)
        header.resize(600,100)
        header.setObjectName("header")
        self.layouts['header']= QHBoxLayout()
            #main title
        self.mainTitle= QLabel(title, header)
            #main menu
        self.mainMenu= QMenuBar(header)
        self.mainMenu.addMenu("Search")
        self.mainMenu.addMenu("Documentation")
        self.mainMenu.addMenu("Quit")
        
        
        
        
        
        #header layout management
        self.layouts['header'].addWidget(self.mainTitle)
        self.layouts['header'].addWidget(self.mainMenu)
        
        header.setLayout(self.layouts['header'])
        
    
            
        # self.container= QWidget(self)
        # self.label= QLabel(self.container)
        
        # self.input= QLineEdit(self.container)
        # self.input.textChanged.connect(self.label.setText)
        
        # self.button= QPushButton("Push me",self.container)
        # self.button.clicked.connect(self.button_clicked)
        # self.button.released.connect(self.button_released)
        
        
        # layout= QVBoxLayout(self.container)
        # layout.addWidget(self.label)
        # layout.addWidget(self.input)
        # layout.addWidget(self.button)
        # self.container.setLayout(layout)
        # self.setCentralWidget(self.container)
        
        
        
    def button_clicked(self):
        self.button.setStyleSheet()
        
    def button_released(self):
        self.button.clearFocus()



if __name__ == '__main__':
    app= QApplication(sys.argv)
    window= HowdoAIV_MainWindow("HowdoAIV", 600, 100)
    window.show()
    app.exec_()