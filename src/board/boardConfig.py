from board.board import Board
    
class BoardConfigItem:
    def __init__(self, name, pos_x, pos_y, height, width, borderHeight, borderWidth, defaultContents, children):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.borderHeight = borderHeight
        self.borderWidth = borderWidth
        self.defaultContents = defaultContents
        self.children = children
        
    def __repr__(self):
        return f"<{self.name}: ({self.pos_x}, {self.pos_y}), ({self.height}, {self.width})>"
    
    def toBoard(self):
        newBoard = Board(self.height, self.width, (self.pos_x, self.pos_y), self.borderHeight, self.borderWidth)
        for index, content in enumerate(self.defaultContents):
            newBoard.setContent(index, content)
        for name, child in self.children.items():
            child.pos_x += self.pos_x
            child.pos_y += self.pos_y
            newBoard.addChild(name, child.toBoard())
        return newBoard