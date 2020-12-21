# -*- coding:utf-8 -*-
'''
【问题】请使用 * 打印出如下
* * * * *
 * * * *
  * * *
   * *
    *
'''

print("Method one:")
# list1 = list(range(5))
# list2 = list1[::-1]
for i in reversed(list(range(5))):
    print("* "*(i+1))
    print(" "*(int(len(list(range(5))))-i),end="" )

print("\nMethod two:")
for i in range(1,6):
    for k in range(i-1):
        print(end=" ")
    for j in range(6-i):
        print("*",end=" ")
    print()