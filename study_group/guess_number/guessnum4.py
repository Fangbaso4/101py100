# encoding:utf-8
from random import randint

# 获取玩家记录
with open("game_one_user.txt","r",encoding="utf-8") as f:
    data = f.read()

listone = data.split()
# print(listone)

# 获取玩家姓名,输出提示
name = listone[0]
hisavg = round(int(listone[3])/int(listone[1]),2)
print(f"{name},你已经玩了{listone[1]}次，最少{listone[2]}轮猜出答案，平均{hisavg}轮猜出答案，开始游戏！")

A = randint(1,100)
times = 0
flag = False
sum_times = int(listone[3])
all_times = [int(listone[2])]


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
        all_times.append(times)
        rounds = len(all_times) + int(listone[1])
        min_times = min(all_times)
        sum_times += times
        avg_times = sum_times / rounds
        print(f"厉害＾▽＾ {name}，你已经玩了{rounds}次，最少{min_times}轮猜出答案，平均{avg_times:.2f}轮猜出答案")
        print("是否继续游戏？（输入y继续，其他退出）")
        replay = str(input("> "))
        if replay.lower() == 'y':
            A = randint(1,100)
            times = 0
            flag = False
        else:
            flag = True
            print("退出游戏，欢迎下次再来")
            f = open('game_one_user.txt','w')
            f.write(f"{name} {rounds} {min_times} {sum_times}")
            f.close()
