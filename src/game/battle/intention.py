from game.action.action import Action
from game.action.interact import AttackInteract, DefenceInteract

class Intention(Action):
    def __init__(self, subject, target):
        super().__init__()
        self.subject = subject
        self.target = target
    
    
class AttackIntention(Intention):
    def __init__(self, subject, target, damage):
        super().__init__(subject, target)
        self.damage = damage
        
    def effect(self):
        AttackInteract(self.subject, self.target, self.damage).execute()
        
    

class DefenceIntention(Intention):
    def __init__(self, subject, target, count):
        super().__init__(subject, target)
        self.count = count
        
    def effect(self):
        DefenceInteract(self.subject, self.target, self.count).execute()