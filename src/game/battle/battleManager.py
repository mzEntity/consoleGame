from others.singleton import singleton
from game.action.stage import *
from game.action.round import *
from game.battle.enemy import *

@singleton
class BattleManager:
    def __init__(self, battleInfo):
        self.battleInfo = battleInfo
        
    def startBattle(self):
        self.battleInfo.drawDeck.shuffle()
        while not self.battleInfo.isOver:
            self.startRound()
        
    def startRound(self):
        PlayerRound(RoundStartStage(), DrawCardStage(), DiscardStage(), RoundEndStage()).execute()
        for enemy in self.battleInfo.enemyList:
            intention = enemy.decideIntention()
            EnermyRound(intention).execute()
    
        allEnemyDied = True
        for enemy in self.battleInfo.enemyList:
            if enemy.hp > 0:
                allEnemyDied = False
                break
        
        roleDied = self.battleInfo.role.hp <= 0
        if roleDied:
            self.battleInfo.isOver = True
            print("血量不足，失败")
        elif allEnemyDied:
            self.battleInfo.isOver = True
            print(f"胜利！还剩{self.battleInfo.role.hp}血量")
                