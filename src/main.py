from utils.pretty import *
from board.boardConfig import *
from utils.cursor import *
import os

def demo(height, width):    
    card_space_dict = dict()
    cardWidth = 15
    cardCount = 10
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
            "battlefield-bar": BoardConfigItem(
                "battlefield-bar", 7, 0, 24, width, 1, 1, [], 
                {
                    "player-space": BoardConfigItem("player-space", 3, 10, 18, width // 4, 1, 1, [], {}),
                    "enemy-space": BoardConfigItem("enemy-space", 3, 10 + width // 3, 18, width // 4, 1, 1, [], {}),
                    "detail-space": BoardConfigItem("detail-space", 0, width - width // 5, 24, width // 5, 1, 1, [], {})
                }
            ),
            "card-bar": BoardConfigItem("card-bat", 30, 0, 12, width, 1, 1, [], card_space_dict)
        }
    )
    
    scene = sceneConfig.toBoard()
    scene.show()

if __name__ == "__main__":
    height = 40
    width = 160
    os.system("cls")
    print("请调整控制台字体大小,使得下面一横一竖两条参考线(包括end)能显示完全:")
    print("*" * (width - 3) + "end")
    for _ in range(height - 2):
        print("*")
    print("end")
    os.system("pause")
    os.system("cls")
    demo(height, width)
