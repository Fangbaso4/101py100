def save_even(n):
    even_list = []
    count = 0
    while len(even_list) < n:
        print ("请输入一个整数")
        num = int(input("> "))
        count += 1
        if num%2 == 0:
            print(f"你输入的数字是{num},是偶数")
            even_list.append(num)
        else:
            print(f"你输入的数字是{num},不是偶数")
    print("你一共输入了{}个数字,其中{}个为偶数，分别是：".format(count,n),end="")
    print(even_list)

save_even(3)
