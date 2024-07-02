from game.action.action import Action
from game.action.interact import AttackInteract, DefenceInteract

class LogicalCard(Action):
    def __init__(self):
        super().__init__()
        self.role = None
        self.target = None
        
    def setTarget(self, role, target):
        self.role = role
        self.target = target
    
    
class AttackCard(Action):
    def __init__(self):
        super().__init__()
    
    
class SkillCard(Action):
    def __init__(self):
        super().__init__()
    
          
class AbilityCard(Action):
    def __init__(self):
        super().__init__()
        

class Attack_S_01(AttackCard):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        AttackInteract(self.role, self.target, 6)
        
        
class Skill_S_01(SkillCard):
    def __init__(self):
        super().__init__()
    
    def effect(self):
        DefenceInteract(self.role, self.target, 5)