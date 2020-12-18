import math

def methodA(n):
    sumA = 0
    for i in range(n+1):
        sumA += i
    print(sumA)

def methodB(n):
    sumB = 1 + n
    if n%2 == 0:
        print((n/2)*sumB)
    else :
        print((math.floor(n/2)*sumB + math.ceil(n/2)))
        
methodA(100)
methodB(100)
