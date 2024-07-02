from others.singleton import singleton
from game.card.deck import *
from game.role.role import Role

@singleton
class BattleInfo:
    def __init__(self):
        pass
    
    def init(self, role):
        self.role = role
        
    def renew(self, enemyList):
        self.drawDeck = Deck(self.role.cardList)
        self.discardDeck = Deck([])
        self.handDeck = Deck([])
        self.enemyList = enemyList
        self.isOver = False
        
    def getRole(self):
        return self.role
        
    