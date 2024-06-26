from utils.pretty import *
from board.boardConfig import *
from utils.cursor import *
import os
import shutil

def demo(height, width):    
    card_space_dict = dict()
    cardHeight = 10
    cardWidth = 15
    cardCount = width // cardWidth
    for i in range(cardCount):
        card_space_dict[f"card-space_{i}"] = BoardConfigItem(f"card-space_{i}", 0, i * cardWidth - i, cardHeight, cardWidth, 1, 1, [], {})
        
    deck_space_dict = dict()
    deckHeight = 10
    deckWidth = 15
    deckColumnCount = width // deckWidth
    deckRowCount = height // deckHeight
    for i in range(deckRowCount):
        for j in range(deckColumnCount):
            deck_space_dict[f"deck-space_{i}_{j}"] = BoardConfigItem(f"deck-space_{i}_{j}", i * deckHeight - i, j * deckWidth - j, deckHeight, deckWidth, 1, 1, [], {})
    
    
    topBarHeight = 3
    topBarWidth = width
    
    hpWidth = 12
    levelWidth = 5
    
    reliqueBarStartRow = 2
    reliqueBarHeight = 5
    reliqueBarWidth = width
    
    battleFieldStartRow = reliqueBarStartRow + reliqueBarHeight - 1
    battleFieldHeight = height // 2
    battleFieldWidth = width
    playerStartColumn = 0
    playerSpaceWidth = width // 4
    enemyStartColumn = playerSpaceWidth - 1
    enemySpaceWidth = width // 4
    
    detailStartColumn = enemyStartColumn + enemySpaceWidth - 1
    detailSpaceWidth = battleFieldWidth - detailStartColumn
    
    cardBarStartRow = battleFieldStartRow + battleFieldHeight - 1
    cardBarHeight = height - cardBarStartRow
    cardBarWidth = width
    sceneConfig = BoardConfigItem(
        "main-scene", 0, 0, height, width, 1, 1, [], 
        {
            "top-bar": BoardConfigItem(
                "top-bar", 0, 0, topBarHeight, topBarWidth, 1, 1, [], 
                {
                    "hp": BoardConfigItem("hp", 1, 1, 1, hpWidth, 0, 0, ["❤️95/100"], {}),
                    "level": BoardConfigItem("level", 1, 1 + hpWidth, 1, levelWidth, 0, 0, ["3-1"], {}),
                }
            ),
            "relique-bar": BoardConfigItem("relique-bar", reliqueBarStartRow, 0, reliqueBarHeight, reliqueBarWidth, 1, 1, [], {}),
            "battlefield-bar": BoardConfigItem(
                "battlefield-bar", battleFieldStartRow, 0, battleFieldHeight, battleFieldWidth, 1, 1, [], 
                {
                    "player-space": BoardConfigItem("player-space", 0, playerStartColumn, battleFieldHeight, playerSpaceWidth, 1, 1, [], {}),
                    "enemy-space": BoardConfigItem("enemy-space", 0, enemyStartColumn, battleFieldHeight, enemySpaceWidth, 1, 1, [], {}),
                    "detail-space": BoardConfigItem("detail-space", 0, detailStartColumn, battleFieldHeight, detailSpaceWidth, 1, 1, [], {})
                }
            ),
            "card-bar": BoardConfigItem("card-bat", cardBarStartRow, 0, cardBarHeight, cardBarWidth, 1, 1, [], card_space_dict)
        }
    )
    
    deckConfig = BoardConfigItem(
        "deck-scene", 0, 0, height, width, 1, 1, [], deck_space_dict
    )
    
    
    mainScene = sceneConfig.toBoard()
    deckScene = deckConfig.toBoard()
    
    # mainScene.show()
    deckScene.show()
    

if __name__ == "__main__":
    size = shutil.get_terminal_size()
    columns = size.columns
    lines = size.lines
    
    height = lines * 3 // 4
    width = columns * 3 // 4
    os.system("cls")
    
    cp1 = record()
    cnewline(height + 2)
    cprint(colored_text("go on...", font_color="purple"))
    cp2 = record()
    
    goto(cp1)
    demo(height, width)
    goto(cp2)
    
