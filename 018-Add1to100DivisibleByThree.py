
# 统计 1 到 100 偶数之和

def methodA(n):
    sumA = 0
    for i in range(n+1):
        if i%3 == 0:
            sumA += i
    print(sumA)


        
methodA(100)

