# 200 coupon
"""
很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。
现在，请你帮他们设计并生成200个优惠券号码：
优惠码的字符由26个英文字符（大小写）组成
每个优惠码有8位
"""
import random as rd

Snum = ord('A')
Enum = ord('Z')
snum = ord('a')
enum = ord('z')
coupon_dic = {}

for i in range(0,200):
    coupon=''
    for j in range(0,8):
        cap = rd.randint(Snum,Enum)
        #print('cap_letter:'+chr(cap))
        low = rd.randint(snum,enum)
        #print('low_letter' + chr(low))
        coupon =coupon + rd.choice([chr(cap),chr(low)])
    if coupon not in coupon_dic.values():
        coupon_dic[i] = coupon
    
print(coupon_dic)    


# -*- coding: utf-8 -*- 参考代码
import random
import string

# 循环200次，生成200个优惠券号码
for i in range(0, 200):
    # 使用默认的52个字符列表（26个字母，大小写）并转换成list
    a = list(string.ascii_letters)
    # 使用shuffle函数把list乱序
    random.shuffle(a)
    # 取乱序后的list的前8个字符连接成字符串，打印到屏幕
#    print(''.join(a[:8]))
