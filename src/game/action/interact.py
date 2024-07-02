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
        prevArmor = self.target.armor
        prevHp = self.target.hp
        armorRemoved = self.damage
        if armorRemoved > prevArmor:
            armorRemoved = prevArmor
        
        hpRemoved = self.damage - armorRemoved
        self.target.armor -= armorRemoved
        self.target.hp -= hpRemoved
        print(f"{self.subject.name}对{self.target.name}造成{self.damage}点伤害，护甲: {prevArmor} -> {self.target.armor}，生命: {prevHp} -> {self.target.hp}")
        
        
class DefenceInteract(Interact):
    def __init__(self, subject, target, count):
        super().__init__(subject, target)
        self.count = count
        
    def effect(self):
        prevArmor = self.target.armor
        self.target.armor += self.count
        print(f"{self.subject.name}获得护甲: {prevArmor} -> {self.target.armor}")