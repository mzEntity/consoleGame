from game.action.action import Action

class PlayerRound(Action):
    def __init__(self, roundStart, drawCard, discard, roundEnd):
        super().__init__()
        self.roundStart = roundStart
        self.drawCard = drawCard
        self.discard = discard
        self.roundEnd = roundEnd
    
    def effect(self):
        print("开始角色回合")
        self.roundStart.execute()
        self.drawCard.execute()
        self.discard.execute()
        self.roundEnd.execute()
        
        
class EnermyRound(Action):
    def __init__(self, description):
        super().__init__()
        self.description = description
    
    def effect(self):
        print(f"敌人进行{self.description}")