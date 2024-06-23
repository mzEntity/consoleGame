from utils.pretty import *
from board.boardConfig import *
from utils.cursor import *
import os

def demo():
    height = 30
    width = 130
    
    card_space_dict = dict()
    cardWidth = 15
    cardCount = 8
    for i in range(cardCount):
        card_space_dict[f"card-space_{i}"] = BoardConfigItem(f"card-space_{i}", 0, i * cardWidth - i, 12, cardWidth, 1, 1, [], {})
    
    sceneConfig = BoardConfigItem(
        "main-scene", 0, 0, height, width, 1, 1, [], 
        {
            "top-bar": BoardConfigItem(
                            "top-bar", 0, 0, 3, width, 1, 1, [], 
                            {
                                "hp": BoardConfigItem("hp", 1, 1, 1, 12, 0, 0, ["❤️95/100"], {}),
                                "level": BoardConfigItem("level", 1, 13, 1, 5, 0, 0, ["3-1"], {}),
                            }
                        ),
            "relique-bar": BoardConfigItem("relique-bar", 2, 0, 6, width, 1, 1, [], {}),
            "card-bar": BoardConfigItem("card-space", 20, 0, 12, width, 1, 1, [], card_space_dict)
        }
    )
    
    scene = sceneConfig.toBoard()
    scene.show()

if __name__ == "__main__":
    os.system("cls")
    demo()
