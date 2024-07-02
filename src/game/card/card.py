
class PhysicalCard:
    def __init__(self, logicalCard):
        self.logicalCard = logicalCard
    
    def play(self):
        self.logicalCard.execute()
    

        