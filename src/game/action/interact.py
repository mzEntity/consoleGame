from game.action.action import Action

class Interact(Action):
    def __init__(self, subject, target):
        super().__init__()
        self.subject = subject
        self.target = target


class AttackInteract(Interact):
    def __init__(self, subject, target, damage):
        super().__init__(subject, target)
        self.damage = damage
        
    def effect(self):
        armorRemoved = self.damage
        if armorRemoved > self.target.armor:
            armorRemoved = self.target.armor
        hpRemoved = self.damage - armorRemoved
        self.target.armor -= armorRemoved
        self.target.hp -= hpRemoved
        print(f"造成{hpRemoved}伤害")
        
        
class DefenceInteract(Interact):
    def __init__(self, subject, target, count):
        super().__init__(subject, target)
        self.count = count
        
    def effect(self):
        self.target.armor += self.count