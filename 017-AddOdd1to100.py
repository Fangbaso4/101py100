
# 统计 1 到 100 偶数之和

def methodA(n):
    sumA = 0
    for i in range(n+1):
        if i%2 == 1:
            sumA += i
    print(sumA)

def methodB(n):
    
    if n%2 == 0:
        sumB =  n
        if (n/2)%2 == 0:
            print( ((n)/4) * sumB )
        else:
            print( ((n-2)/4) * sumB + n/2)
    else :
        sumB = 1 + n
        print(((n-1)/4)*sumB + ((n+1)/2))
        
methodA(100)
methodB(100)
