import time
from PySide2.QtWidgets import (QPushButton, QLabel, QLineEdit,QWidget,
                               QVBoxLayout)


class HowdoAIV_Button(QPushButton):
    
    def __init__(self, text, parent):
        super().__init__(text, parent)
        

class HowdoAIV_Timer:
    
    @property
    def is_running(self):
        return self.running
    
    def __init__(self, duration):
        self.timer=0
        self.duration= duration
        self.current_tick_time= 0
        self.last_tick_time= 0
        self.running= False
        
        
    def start(self):
        self.reset()
        self.running= True
        
    def tick(self):
        if self.is_running:
            self.last_tick_time= self.current_tick_time
            self.current_tick_time= time.time()
            
            self.timer-=self.current_tick_time-self.last_tick_time
            
            if self.timer<=0:
                self.stop()
        
    def stop(self):
        self.running= False
        
    def reset(self):
        self.timer= self.duration
        self.current_tick_time= time.time()
        