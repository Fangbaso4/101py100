#【问题】取一个整数a从右端开始的4〜7位，如 431421467，输出 1421。


def methodA(n):
    print("THIS IS METHODA")
    listA = list(str(n))
    stringA = ''.join(listA[-7:-3])
    print (stringA)


def methodB(n):
    print("THIS IS METHODB")
    stringB = str(n)[-7:-3]
    print(stringB)
        
methodA(431421467)
methodB(431421467)
