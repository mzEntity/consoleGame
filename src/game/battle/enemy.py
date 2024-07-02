import random
from game.battle.intention import *
from game.role.role import Role

class Enemy:
    def __init__(self, name, hp, maxHp, armor):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.armor = armor
        self.target = Role()
        
        
    def decideIntention(self):
        intention = random.choice([AttackIntention(self, self.target, 8), DefenceIntention(self, self, 8)])
        return intention