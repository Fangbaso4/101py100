# -*- coding: UTF-8 -*-
print("method one:-------------------")
print("请输入利润值(单位：万元)：")
I = float(input("> "))

if I <= 10:
    bonus = I * 0.1
elif I > 10 and I <= 20:
    bonus = 10 * 0.1 + (I - 10) * 0.075
elif I > 20 and I <= 40:
    bonus = 10 * 0.1 + (20 - 10) * 0.075 + (I - 20) * 0.05
elif I> 40 and I <= 60:
    bonus = 10 * 0.1 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + (I - 40) * 0.03
elif I > 60 and I <=100:
    bonus = 10 * 0.1 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + ( 60- 40) * 0.03 + (I - 60) * 0.015
else :
    bonus = 10 * 0.1 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + ( 60- 40) * 0.03 + (100 - 60) * 0.015 + (I - 100) * 0.01

print("应发奖金：{}万元".format(bonus))

print("method two:-------------------")
 
print("请输入利润值(单位：万元)：")
i = float(input("> "))
arr = [100,60,40,20,10,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        # print((i-arr[idx])*rat[idx])
        i=arr[idx]
print('应发奖金总数%.2f万元'%r)


print("method three:-------------------")