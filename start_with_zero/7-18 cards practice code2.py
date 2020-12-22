# -*- coding: UTF-8 -*-
import random
import time

#黑桃（Spade）、红桃（Heart）、方块（Diamond）、梅花（Club）
cardType = ['Spade  ','Heart    ','Diamond  ','Club ']
cardNum =  ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

#生成54张卡牌
def genderCards():
    cardPairs = []
    #嵌套循环生成52张花色牌
    for type in cardType:
        for num in cardNum:
            cardPairs.append((type,num))
    
    #添加joker
    cardPairs.append('joker') #小王
    cardPairs.append('JOKER') #大王
    
    return (cardPairs)

#分配牌
def dispatchCards(cardPairs):
    #洗牌
    shuffleTimes=int(input('请输入洗牌次数:'))
    for i in range(0,shuffleTimes):
        random.shuffle(cardPairs)
    #玩家手牌列表
    playerA_Cards = []
    playerB_Cards = []
    playerC_Cards = []
    bottomCardNum = 3 #底牌数量
    for index in range(0,len(cardPairs) - bottomCardNum):
        cardPair = cardPairs[index]
        #使用余数值进行判断发牌
        if index % 3 == 0:  #玩家A
            playerA_Cards.append(cardPair)
        elif index % 3 == 1:    #玩家B
            playerB_Cards.append(cardPair)
        else:   #玩家C
            playerC_Cards.append(cardPair)


        #展示各个玩家手牌
        print("玩家A 手牌：",len(playerA_Cards))
        for cardPair in playerA_Cards:
            print(' '.join(cardPair))
        print('\n')
        
        print("玩家B 手牌：",len(playerB_Cards))
        for cardPair in playerB_Cards:
            print(' '.join(cardPair))
        print('\n')

        print("玩家C 手牌：",len(playerC_Cards))
        for cardPair in playerC_Cards:
            print(' '.join(cardPair))
        print('\n')

        #展示当前已发出的牌
        #print(' '.join(cardPair),end='\t')
        time.sleep(0.1) #停顿展示
    print('\n')

    
    
    print("底牌：",bottomCardNum)
    rest_cards = cardPairs[-3:]
    for cardPair in rest_cards:
        print(' '.join(cardPair))

#生成牌面
cardPairs = genderCards()
# 分配牌    
dispatchCards(cardPairs)

