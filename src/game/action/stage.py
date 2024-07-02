from game.action.action import Action
from game.action.energy import ObtainEnergyAction, LoseEnergyAction
from game.action.card import DrawCardAction, DiscardCardAction, PlayCardAction
from game.action.logicalCard import *

class Stage(Action):
    def __init__(self):
        super().__init__()
    
class RoundStartStage(Stage):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        curEnergy = self.battleInfo.role.energy
        energyPerRound = self.battleInfo.role.energyPerRound
        LoseEnergyAction(curEnergy).execute()
        ObtainEnergyAction(energyPerRound).execute()
        
class DrawCardStage(Stage):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        cardPerRound = self.battleInfo.role.cardPerRound
        DrawCardAction(cardPerRound).execute()
        
class PlayStage(Stage):
    def __init__(self):
        super().__init__()
        self.isOver = False
        
    def effect(self):
        handDeck = self.battleInfo.handDeck
        for _ in range(3):
            card = handDeck.cardList[0]
            if isinstance(card, Attack_S_01):
                PlayCardAction(card, self.battleInfo.role, self.battleInfo.enemyList[0]).execute()
            else:
                PlayCardAction(card, self.battleInfo.role, self.battleInfo.role).execute()

class DiscardStage(Stage):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        handDeck = self.battleInfo.handDeck
        DiscardCardAction(handDeck).execute()

class RoundEndStage(Stage):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        pass