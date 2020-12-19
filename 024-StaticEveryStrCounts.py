#【问题】从控制台输入一段字符，统计各字符出现次数


def methodA(n):
    print("THIS IS METHODA\n请输入一段字符：")
    strA = input("> ")
    dictA = {}
    for i in strA :
       dictA[i] = dictA.get(i, 0)+1
    for i in dictA:
        print("字符：{}，出现次数{}。".format(i,dictA[i]))

def methodB(n):
    print("THIS IS METHODB\n请输入一段字符：")
    strB = input("> ")
    listB = list(strB)
    for i in listB:
        print("字符：{}，出现次数{}。".format(i,listB.count(i)))
    
        
methodA("")
methodB("")

