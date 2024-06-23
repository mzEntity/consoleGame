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
        self.end = CursorPosition(position[0] + height, 0)
        
        self.children = dict()
        
    def show(self):
        goto(self.start)
        for _ in range(self.borderHeight):
            cprint("*" * self.width)
            cnewline_indent(self.start)
        
        contentsLength = len(self.contents)
        for i in range(self.contentHeight):
            content = ""
            if i < contentsLength:
                content = self.contents[i]
            if i >= self.contentHeight:
                break            
            displayContent = content.ljust(self.contentWidth)[:self.contentWidth]
            cprint("*" * self.borderWidth + displayContent + "*" * self.borderWidth)
            cnewline_indent(self.start)
        for _ in range(self.borderHeight):
            cprint("*" * self.width)
            cnewline_indent(self.start)
            
        for _, child in self.children.items():
            child.show()
            
    def setContent(self, lineIndex, content):
        if lineIndex > self.contentHeight:
            return
        self.contents[lineIndex] = content
        
    def addChild(self, name, board):
        self.children[name] = board
    
    
        
    
        
            
        