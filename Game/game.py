# -*- coding:utf-8 -*-
# @Time : 2020/5/15 14:08 
# @Author : Zhang Jingyao
# @File : game.py 
# @Software: PyCharm

class Gamer:
    def __init__(self, hp=1000, powers=200):
        self.hp = hp
        self.powers = powers

    def fight(self, enemy_power, ememy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = ememy_hp - self.powers


gamer = Gamer()
print(gamer.hp)
print(gamer.powers)
