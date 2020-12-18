
# 统计 1 到 100 偶数之和

def methodA(n):
    sumA = 0
    for i in range(n+1):
        if i%2 ==0:
            sumA += i
    print(sumA)

def methodB(n):
    sumB = 2 + n
    if n%2 == 0:
        print( ((n-2)/4) * sumB + ((n+2)/2))
    else :
        print(((n-1)/4)*sumB)
        
methodA(100)
methodB(100)
