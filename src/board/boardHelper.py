from others.singleton import singleton

from board.board import Board

@singleton
class BoardHelper:
    def __init__(self):
        self.boardDict = dict()
        
    def config(self, boardConfigList):
        for item in boardConfigList:
            newBoard = Board(item.height, item.width, (item.pos_x, item.pos_y), item.borderHeight, item.borderWidth)
            for index, content in enumerate(item.defaultContents):
                newBoard.setContent(index, content)
            self.boardDict[item.name] = newBoard
        
    def showBoard(self):
        for _, board in self.boardDict.items():
            board.show()
            
    def setBoard(self, boardName, board):
        self.boardDict[boardName] = board
        
    def getBoard(self, boardName):
        if boardName in self.boardDict:
            return self.boardDict[boardName]
        else:
            return None
            
    
class BoardConfigItem:
    def __init__(self, name, pos_x, pos_y, height, width, borderHeight, borderWidth, defaultContents):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.borderHeight = borderHeight
        self.borderWidth = borderWidth
        self.defaultContents = defaultContents
        
    def __repr__(self):
        return f"<{self.name}: ({self.pos_x}, {self.pos_y}), ({self.height}, {self.width})>"