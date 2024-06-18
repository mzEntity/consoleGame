from utils.pretty import *
from utils.cursor import *
import time


class Board:
    def __init__(self, height, width, cursorPosition):
        self.height = height
        self.width = width
        self.contents = []
        self.start = cursorPosition
        
    def show(self, color):
        goto(self.start)
        cprint(colored_text("*" * self.width + "\n", font_color=color))
        for _ in range(self.height - 2):
            cprint(colored_text("*" + " " * (self.width - 2) + "*" + "\n", font_color=color))
        cprint(colored_text("*" * self.width + "\n", font_color=color))
    

        
        
def demo(count):
    height = 10
    width = 15
    cp = record()
    b = Board(height, width, cp)
    for _ in range(count):
        b.show("red")
        time.sleep(1)
        b.show("yellow")
        time.sleep(0.5)
        b.show("green")
        time.sleep(1)
        b.show("yellow")
        time.sleep(0.5)
    
        
    
        
            
        