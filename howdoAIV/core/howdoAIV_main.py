from howdoAIV_howdoi_parser import HowdoAIV_Parser
from howdoAIV_custom_widgets import HowdoAIV_Button, HowdoAIV_Timer
from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QScrollArea)
from math import floor
import webbrowser
import sys


class HowdoAIV_MainWindow(QMainWindow):
    
    def __init__(self, title, app,x, y, width, height):
        super().__init__()
        #main window settings
        self.setWindowTitle(title)
        self.app= app
        self.full_size_app= False
        self.x=x
        self.y= y
        self.default_width= width
        self.default_height= height
        self.current_height= self.default_height
        self.full_size_height= 800
        self.anim_timer= HowdoAIV_Timer(0.25)
        self.setFixedSize(width,height)
        self.howdoi_parser= HowdoAIV_Parser()
        self.move(self.x,self.y)
        
        
        #stylesheet management 
        with open('..\stylesheets\window.qss','r') as stylesheet:
            self._style = stylesheet.read()
        self.setStyleSheet(self._style)
        
        #layouts dictionary
        self.layouts= {}
        self.layouts['window']= QVBoxLayout()
        self.setLayout(self.layouts['window'])
        
        #header
        self.header = QWidget(self)
        self.header.resize(600,100)
        self.header.setObjectName("header")
        self.layouts['header']= QHBoxLayout()
        self.header.setLayout(self.layouts['header'])
        
        
            #main title
        self.main_title= QLabel(title, self.header)
            #main menu
        self.main_menu= QWidget(self.header)
        self.search_btn = HowdoAIV_Button("SEARCH", self.main_menu)
        self.search_btn.clicked.connect(self.search_btn_clicked)
        
        self.about_btn= HowdoAIV_Button("ABOUT", self.main_menu)
        self.about_btn.clicked.connect(self.about_btn_clicked)
        
        self.quit_btn= HowdoAIV_Button("QUIT", self.main_menu)
        self.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.layouts['main_menu']= QHBoxLayout()
        self.main_menu.setLayout(self.layouts['main_menu'])
        
         #body
        self.body= QWidget(self)
        self.body.resize(600,700)
        self.body.setObjectName("body")
        self.layouts['body']= QVBoxLayout()
        self.body.setLayout(self.layouts['body'])
        
            #textarea
        self.output_area= QTextEdit("<b>How do I?</b>\n",self.body)
        self.input_area= QLineEdit(self.body)
        self.input_area.returnPressed.connect(self.howdoAIV_send_request)
        
        
        #header layout management
        
        self.layouts['window'].addWidget(self.header)
        self.layouts['window'].addWidget(self.body)
        
        self.layouts['header'].addWidget(self.main_title)
        self.layouts['header'].addWidget(self.main_menu)
        
        self.layouts['main_menu'].addWidget(self.search_btn)
        self.layouts['main_menu'].addWidget(self.about_btn)
        self.layouts['main_menu'].addWidget(self.quit_btn)
        
        self.layouts['body'].addWidget(self.output_area)
        self.layouts['body'].addWidget(self.input_area)
        
        self.body.move(0,100)
        self.show()
        self.body.hide()
            
        
    def search_btn_clicked(self):
        if not self.full_size_app:
            self.current_height= self.default_height
            self.anim_timer.start()
            while self.anim_timer.is_running:
                self.anim_timer.tick()
                fraction = (self.anim_timer.duration-self.anim_timer.timer)/self.anim_timer.duration
                height_fraction= floor((self.full_size_height-self.default_height)*fraction)
                self.current_height= floor(self.default_height+height_fraction)
                self.setFixedHeight(self.current_height)
            self.setFixedHeight(self.full_size_height)
            self.full_size_app= True
            self.body.show()
        
    def about_btn_clicked(self):
        webbrowser.open('https://github.com/gleitz/howdoi') 
        
    def quit_btn_clicked(self):
        self.app.quit()
        
    def howdoAIV_send_request(self):
        query= self.howdoi_parser.howdoAIV_query(self.input_area.text())
        self.output_area.setText(query)
        



if __name__ == '__main__':
    app= QApplication(sys.argv)
    window_w=600
    window_h=100
    window_x= app.primaryScreen().size().width() *0.5 - window_w*0.5
    window_y= 100
    window= HowdoAIV_MainWindow("HowdoAIV",app, window_x, window_y, window_w, window_h)
    app.exec_()
    