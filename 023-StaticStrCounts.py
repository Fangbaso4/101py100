#【问题】从控制台输入一段字符，统计字符'b'出现次数

def methodA(n):
    print("THIS IS METHODA\n请输入一段字符：")
    strA = input("> ")
    countA = 0
    for i in strA:
        if i == n:
            countA += 1
        
    print("你输入的字符串是{}，其中有{}个{}".format(strA,countA,n))

def methodB(n):
    print("THIS IS METHODB\n请输入一段字符：")
    strB = input("> ")
    countB = len(strB) - len(strB.replace(n,""))
        
    print("你输入的字符串是{}，其中有{}个{}".format(strB,countB,n))

        
methodA("b")        
methodB("b")

