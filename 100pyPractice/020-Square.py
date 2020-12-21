#【问题】输入数字，如果平方运算后小于 50 则退出。


def methodA(n):
    print("THIS IS METHODA")
    while True:
        print("请输入一个数字：")
        num = float(input("> "))
        sumA = 1
        for i in range(2):
            sumA = sumA*num
        print(sumA)
        if sumA < n:
            break
        else:
            continue


def methodB(n):
    print("THIS IS METHODB")
    while True:
        print("请输入一个数字：")
        num = float(input("> "))
        sumB = num ** 2
        print(sumB)
        if sumB < n:
            break
        else:
            continue
        
methodA(50)
methodB(50)
