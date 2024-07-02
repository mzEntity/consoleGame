from game.action.action import Action
from game.action.energy import ObtainEnergyAction, LoseEnergyAction
from game.action.card import DrawCardAction, DiscardCardAction

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

class DiscardStage(Stage):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        DiscardCardAction().execute()

class RoundEndStage(Stage):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        pass