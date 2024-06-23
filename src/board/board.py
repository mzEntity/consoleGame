from utils.pretty import *
from utils.cursor import *
import time


class Board:
    def __init__(self, height, width, position, borderHeight=0, borderWidth=0):
        self.height = height
        self.width = width
        self.borderHeight = borderHeight
        self.borderWidth = borderWidth
        
        self.contentHeight = self.height - 2 * self.borderHeight
        self.contentWidth = self.width - 2 * self.borderWidth
        self.contents = []
        for _ in range(self.contentHeight):
            self.contents.append(" " * self.contentWidth)
        self.start = CursorPosition(position[0], position[1])
        
    def show(self):
        goto(self.start)
        for _ in range(self.borderHeight):
            cprint("*" * self.width + "\n")
            cindent(self.start)
        
        contentsLength = len(self.contents)
        for i in range(self.contentHeight):
            content = ""
            if i < contentsLength:
                content = self.contents[i]
            if i >= self.contentHeight:
                break            
            displayContent = content.ljust(self.contentWidth)[:self.contentWidth]
            cprint("*" * self.borderWidth + displayContent + "*" * self.borderWidth + "\n")
            cindent(self.start)
        for _ in range(self.borderHeight):
            cprint("*" * self.width + "\n")
            cindent(self.start)
            
    def setContent(self, lineIndex, content):
        if lineIndex > self.contentHeight:
            return
        self.contents[lineIndex] = content
    
    
        
    
        
            
        