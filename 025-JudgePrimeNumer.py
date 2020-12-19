#【问题】判断输入数字是否为质数


def methodA(n):
    print("THIS IS METHODA\n请输入一个整数：")
    numA = int(input("> "))
    if (numA%2 == 1 and numA%3 == 1 and numA%5 ==1 and numA%7 ==1)or numA == 3 or numA == 5 or numA ==7:
        print("你输入的{}是质数".format(numA))
    else:
        print("你输入的{}不是质数".format(numA))
        
def methodB(n):
    print("THIS IS METHODB\n请输入一个整数：")
    numB = int(input("> "))
    if numB == 3 or numB == 5 or numB ==7:
        print(f"你输入的整数{numB}是质数")
    elif numB%2 == 0:
        print(f"你输入的整数{numB}除1和{numB}外可以被2整除，不是质数")
    elif numB%3 == 0:
        print(f"你输入的整数{numB}除1和{numB}外可以被3整除，不是质数")
    elif numB%5 == 0:
        print(f"你输入的整数{numB}除1和{numB}外可以被5整除，不是质数")
    elif numB%7 == 0:
        print(f"你输入的整数{numB}除1和{numB}外可以被7整除，不是质数")
    else:
        print(f"你输入的整数{numB}是质数")
    
        
methodA("")
methodB("")

