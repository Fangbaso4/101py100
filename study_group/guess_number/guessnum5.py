# encoding:utf-8
from random import randint

# 获取玩家记录
with open("game_one_user.txt","r",encoding="utf-8") as f:
    data = f.readlines()

listAll=[]
for line in data:
    listAll.append(line)

dicAll = {}
for i in listAll:
    data = i.strip().split()
    # print(data[0],data[1:],data)
    dicAll[data[0]] = data[1:]
# print(dicAll)

# 输入玩家姓名，拉取记录
print("请输入玩家昵称：")
name = input("> ")
if dicAll.get(name) == None:
    listone = ['0','0','0']
    sum_times = int(listone[2])
    all_times = []
    print(f"{name},你还没有玩过，开始游戏！")
else :
    listone = dicAll.get(name)
    hisavg = round(int(listone[2])/int(listone[0]),2)
    sum_times = int(listone[2])
    all_times = [int(listone[1])]
    print(f"{name},你已经玩了{listone[0]}次，最少{listone[1]}轮猜出答案，平均{hisavg}轮猜出答案，开始游戏！")
    # print(dicAll.get(name))

# 游戏部分
## 初始化数据
A = randint(1,100)
times = 0
flag = False
## 进入猜数字
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
        if dicAll.get(name) == None:
            rounds = len(all_times) 
        else:
            rounds = len(all_times) + int(listone[0]) -1
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
            dicAll[name] = [str(rounds),str(min_times),str(sum_times)]
            res = ''
            for i in dicAll:
                line = i + ' ' + ' '.join(dicAll[i]) +'\n'
                res += line
            with open('game_one_user.txt','w',encoding="utf-8") as f:
                f.write(res)