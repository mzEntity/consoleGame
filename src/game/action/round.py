from game.action.action import Action

class PlayerRound(Action):
    def __init__(self, roundStart, drawCard, playCard, discard, roundEnd):
        super().__init__()
        self.roundStart = roundStart
        self.drawCard = drawCard
        self.playCard = playCard
        self.discard = discard
        self.roundEnd = roundEnd
    
    def effect(self):
        print("开始角色回合")
        self.roundStart.execute()
        self.drawCard.execute()
        self.playCard.execute()
        self.discard.execute()
        self.roundEnd.execute()
        
        
class EnermyRound(Action):
    def __init__(self, intention):
        super().__init__()
        self.intention = intention
    
    def effect(self):
        self.intention.execute()