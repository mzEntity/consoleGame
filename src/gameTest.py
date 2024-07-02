import os
from game.action.round import *
from game.action.stage import *
from game.action.energy import *
from game.action.card import *
from game.action.actionConfig import *

from game.battle.battle import *
from game.battle.enemy import Enemy
from game.battle.battleManager import BattleManager

from game.card.deck import Deck
from game.role.role import Role
from game.card.card import PhysicalCard
from game.action.logicalCard import *


def initConfig():
    pass


if __name__ == "__main__":
    os.system("cls")
    print("start playing \"Slay the Spire\".")
    initConfig()
    role = Role(50, 50, [Attack_S_01(), Attack_S_01(), Attack_S_01(), Attack_S_01(), Attack_S_01(), 
                         Skill_S_01(), Skill_S_01, Skill_S_01(), Skill_S_01(), Skill_S_01()], 100)
    battleInfo = BattleInfo()
    battleInfo.init(role)
    enemy = Enemy("史莱姆", 20, 20, 0)
    battleInfo.renew([enemy])
    battleManager = BattleManager(battleInfo)
    battleManager.startBattle()
    print("go on...")