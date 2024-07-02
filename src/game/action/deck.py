from game.action.action import Action

class ShuffleAction(Action):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        drawDeck = self.battleInfo.drawDeck
        discardDeck = self.battleInfo.discardDeck
        
        drawDeck.addTo(discardDeck)
        discardDeck.clear()
        drawDeck.shuffle()
        print("触发洗牌")
        