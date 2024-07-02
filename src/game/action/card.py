from game.action.action import Action
from game.action.deck import ShuffleAction

class DrawCardAction(Action):
    def __init__(self, count):
        super().__init__()
        self.count = count
    
    def effect(self):
        print(f"想要抽{self.count}张牌")
        drawDeck = self.battleInfo.drawDeck
        handDeck = self.battleInfo.handDeck
        
        cardLeftCount = drawDeck.count()
        if cardLeftCount >= self.count:
            tmpDeck = drawDeck.selectTop(self.count)
            handDeck.addTo(tmpDeck)
        else:
            tmpDeck = drawDeck.selectTop(cardLeftCount)
            handDeck.addTo(tmpDeck)
            ShuffleAction().execute()
            count = self.count - cardLeftCount
            if count > drawDeck.count():
                count = drawDeck.count()
            tmpDeck = drawDeck.selectTop(count)
            handDeck.addTo(tmpDeck)
            
        
        
class DiscardCardAction(Action):
    def __init__(self):
        super().__init__()
    
    def effect(self):
        discardDeck = self.battleInfo.discardDeck
        handDeck = self.battleInfo.handDeck
        print(f"弃置手牌{handDeck.count()}张")
        discardDeck.addTo(handDeck)
        handDeck.clear()
        