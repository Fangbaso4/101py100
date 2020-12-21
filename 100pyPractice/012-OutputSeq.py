# -*- coding:utf-8 -*-
# 【问题】输入3个整数a,b,c，按大小顺序输出。


print("输入三个整数，使用空格分隔")
string = input("> ")
lista = string.split()
lista.sort()
for num in lista:
    print(num)