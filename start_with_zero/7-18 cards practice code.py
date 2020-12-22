'''
【问题描述】
三人斗地主手牌规则：
一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。

要求：
将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。
可使用 list 和 random 完成。
'''
import random as rd

flower = ['Spade','Heart','Diamond','Club']#黑桃（Spade）、红桃（Heart）、方块（Diamond）、梅花（Club）
nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card = []
for i in flower:
    for j in nums:
        card.append(i+j)
card.append('joker')
card.append('JOKER')

#METHOD one
rd.shuffle(card)
playerA = card[0:17]
playerB = card[17:34]
playerC = card[34:51]
bottom = card[51:]
print('playerA:'+str(playerA)+'\n'+'playerB:'+str(playerB)
      +'\n'+'playerC:'+str(playerC)+'\n'+'bottom:'+str(bottom))
print('#############')
#METHOD two
i=0
playerA = []
playerB = []
playerC = []
bottom = []
while i < 17:
    a=rd.choice(card)
    playerA.append(a)
    card.remove(a)
    print('playerA:'+str(playerA))
    
    b=rd.choice(card)
    playerB.append(b)
    card.remove(b)
    print('playerB:'+str(playerB))
    
    c=rd.choice(card)
    playerC.append(c)
    card.remove(c)
    print('playerC:'+str(playerC))
    i += 1
print('bottom:'+str(card))
