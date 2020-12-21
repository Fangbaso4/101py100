
#【问题】统计1 到 100 内质数之和

def methodA(n):
    print("This is methodA")
    sumA = 0    
    for numA in range(2,n+1):
            for i in range(2,numA):
                if (numA % i) == 0:
                    break
            else:
                sumA = sumA + numA
    print(sumA)
methodA(100)
