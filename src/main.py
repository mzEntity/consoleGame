from utils.pretty import *
from board.boardHelper import *


def demo():
    helper = BoardHelper()
    height = 30
    width = 100
    configList = [
        BoardConfigItem("scene", 0, 0, height, width, 1, 1, []),
        
        BoardConfigItem("top-bar", 0, 0, 3, width, 1, 1, []),
        BoardConfigItem("hp", 1, 1, 1, 12, 0, 0, ["❤️95/100"]),
        BoardConfigItem("level", 1, 13, 1, 5, 0, 0, ["3-1"]),
        
        BoardConfigItem("relique-bar", 2, 0, 6, width, 1, 1, []),
        BoardConfigItem("card-space", 18, 0, 12, width, 1, 1, [])
    ]
    
    cardWidth = 20
    cardCount = int(width / cardWidth)
    for i in range(cardCount):
        configList.append(BoardConfigItem(f"card-space_{i}", 18, i * cardWidth, 12, cardWidth, 1, 1, []))
    
    helper.config(configList)
    helper.showBoard()

if __name__ == "__main__":
    demo()
