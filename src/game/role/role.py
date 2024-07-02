from others.singleton import singleton

@singleton
class Role:
    def __init__(self, name, hp, maxHp, cardList, money):
        self.name = name
        
        self.hp = hp
        self.maxHp = maxHp
        
        self.armor = 0
        self.energy = 0
        self.energyPerRound = 3
        
        self.cardPerRound = 5
        
        self.cardList = cardList
        self.money = money
        
    
    
    