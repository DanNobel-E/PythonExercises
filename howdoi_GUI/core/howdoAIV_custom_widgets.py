from PySide2.QtWidgets import (QPushButton, QLabel, QLineEdit,QWidget,
                               QVBoxLayout)


class HowdoAIV_Button(QPushButton):
    
    def __init__(self, text, parent):
        super().__init__(text, parent)
        
    