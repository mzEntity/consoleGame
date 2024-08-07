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
        for _ in range(count):
            self.cardList.pop(0)
        return Deck(selectCardList)
    
    def selectFrom(self, cardList):
        for card in cardList:
            if card not in self.cardList:
                PANIC("selectFrom: card not exists.")
            self.cardList.remove(card)
        return Deck(cardList)
    
    def clear(self):
        self.cardList.clear()
                
    def count(self):
        return len(self.cardList)
    