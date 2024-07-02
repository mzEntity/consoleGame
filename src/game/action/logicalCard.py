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
    
    
class AttackCard(LogicalCard):
    def __init__(self):
        super().__init__()
    
    
class SkillCard(LogicalCard):
    def __init__(self):
        super().__init__()
    
          
class AbilityCard(LogicalCard):
    def __init__(self):
        super().__init__()
        

class Attack_S_01(AttackCard):
    def __init__(self):
        super().__init__()
        
    def effect(self):
        AttackInteract(self.role, self.target, 6).execute()
        
        
class Skill_S_01(SkillCard):
    def __init__(self):
        super().__init__()
    
    def effect(self):
        DefenceInteract(self.role, self.target, 5).execute()