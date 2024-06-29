import random
from game.exceptions.exceptions import PANIC

class Deck:
    def __init__(self, cardList):
        self.cardList = cardList
        
    def shuffle(self):
        random.shuffle(self.cardList)
        
    def cardAt(self, index):
        if index >= self.count():
            PANIC("cardAt: index out of bound.")
        return self.cardList[index]
            
    def addTo(self, newDeck):
        count = newDeck.count()
        for i in range(count):
            self.cardList.append(newDeck.cardAt(i))
        newDeck.selectTop(count)
                    
    def selectTop(self, count):
        if count > self.count():
            PANIC("selectTop: you can't select too many cards.")
        selectCardList = []
        for i in range(count):
            selectCardList.append(self.cardList[i])
        self.cardList.pop(list(range(count)))
        return Deck(selectCardList)
                
    def count(self):
        return len(self.cardList)
    