print("method one :")

while True:
    s = str(input("请输入需要获取长度的文字："))
    print(len(s))
    flag = str(input("继续请按 y ,退出请按任意字母："))
    if flag.lower != "y":
        break