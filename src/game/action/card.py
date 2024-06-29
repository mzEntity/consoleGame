from game.action.action import Action

class DrawCardAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        print(f"抽 {self.count} 张牌")
        
        
class DiscardCardAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        if self.count == -1:
            print(f"弃置所有手牌")
        else:
            print(f"弃置 {self.count} 张牌")