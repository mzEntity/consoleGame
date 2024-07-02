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
    def __init__(self, deck):
        super().__init__()
        self.deck = deck
    
    def effect(self):
        discardDeck = self.battleInfo.discardDeck
        print(f"弃置手牌{self.deck.count()}张")
        discardDeck.addTo(self.deck)
        self.deck.clear()
        
        
class PlayCardAction(Action):
    def __init__(self, logicalCard, subject, target):
        super().__init__()
        self.logicalCard = logicalCard
        self.subject = subject
        self.target = target
    
    def effect(self):
        handDeck = self.battleInfo.handDeck
        deck = handDeck.selectFrom([self.logicalCard])
        
        self.logicalCard.setTarget(self.subject, self.target)
        self.logicalCard.execute()
        DiscardCardAction(deck).execute()
        