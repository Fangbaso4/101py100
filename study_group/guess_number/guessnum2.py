# encoding:utf-8

from random import randint

A = randint(1,100)
times = 0
flag = False

while flag is False:
    print('请猜一个1到100的数字')
    gnum = int(input('> ')) 
    times += 1
    if gnum > A:
        print("猜大了，再试试")
    elif gnum < A:
        print("猜小了，再试试")
    else:
        print("猜对了，你一共猜了%d轮"%times )
        print("是否继续游戏？（输入y继续，其他退出）")
        replay = str(input("> "))
        if replay.lower() == 'y':
            A = randint(1,100)
            times = 0
            flag = False
        else:
            flag = True
            print("退出游戏，欢迎下次再来")
             