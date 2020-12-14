# -*- coding:utf-8 -*-
# code 011
'''
【问题】请使用 * 打印出如下
* * * * *
*     *
*   *
* *
*
'''
print("method one:-------")
list1 = list(range(1,6,2))
for row in reversed(range(5)):
    if (row >= 1 and row <=3):
        print("*",end="")
        print(" "*list1[row - 1],end="")
        print("*")
    else:
        print("* "*(row+1))




# for row in range(6):  
#     for col in range(7):  
#         if (row==0 and col %3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):  
#             print("*",end=" ")  
#         else:  
#             print(end=" ")  
#     print() 