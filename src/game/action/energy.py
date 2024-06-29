from game.action.action import Action

class ObtainEnergyAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        print(f"获得能量 {self.count} 点")
        
        
class LoseEnergyAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        if self.count == -1:
            print(f"失去所有能量")
        else:
            print(f"失去能量 {self.count} 点")