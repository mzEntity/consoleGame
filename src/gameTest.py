import os
import random
from game.action.round import *
from game.action.stage import *
from game.action.energy import *
from game.action.card import *
from game.action.actionConfig import *

def initConfig():
    ActionConfig().addMonitorBefore("RoundStartStage", LoseEnergyAction(-1))
    ActionConfig().addMonitorBefore("RoundStartStage", ObtainEnergyAction(3))
    ActionConfig().addMonitorBefore("DrawCardStage", DrawCardAction(5))
    ActionConfig().addMonitorBefore("DiscardStage", DiscardCardAction(-1))


if __name__ == "__main__":
    os.system("cls")
    print("start playing \"Slay the Spire\".")
    initConfig()
    intentions = ["进攻", "防御", "强化", "弱化"]
    for _ in range(10):
        intention = random.choice(intentions)
        PlayerRound(RoundStartStage(), DrawCardStage(), DiscardStage(), RoundEndStage()).execute()
        EnermyRound(intention).execute()
    print("go on...")