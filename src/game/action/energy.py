from game.action.action import Action

class ObtainEnergyAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        self.battleInfo.role.energy += self.count
        
        
class LoseEnergyAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        if self.battleInfo.role.energy < self.count:
            self.battleInfo.role.energy = 0
        else:
            self.battleInfo.role.energy -= self.count