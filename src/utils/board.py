from utils.pretty import *
from utils.cursor import *
import time

def demo(count):
    height = 10
    width = 15
    for _ in range(count):
        show_board(height, width, "red")
        time.sleep(1)
        show_board(height, width, "yellow")
        time.sleep(0.5)
        show_board(height, width, "green")
        time.sleep(1)
        show_board(height, width, "yellow")
        time.sleep(0.5)
    move_cursor_down(height)
        
    
def show_board(height, width, color):
    if height < 2 or width < 2:
        print(colored_text("Both height and width must be no less than 2."))
        return
    print(colored_text("*" * width, font_color=color))
    for _ in range(height - 2):
        print(colored_text("*" + " " * (width - 2) + "*", font_color=color))
    print(colored_text("*" * width, font_color=color))
    move_cursor_up(height)
        
            
        