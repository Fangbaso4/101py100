#!/usr/bin/env python
# coding: utf-8
'''
要求：

读取 report.txt 文件中的成绩；
统计每名学生总成绩、计算平均并从高到低重新排名；
汇总每一科目的平均分和总平均分（见下表第一行）；
添加名次，替换60分以下的成绩为“不及格”；
将处理后的成绩另存为一个新文件（result.txt）
'''
import numpy as np
import pandas as  pd

#读取 report.txt 文件中的成绩；
f = open("report.txt","r",encoding="utf-8")
l = []
for line in f:
    # print(line,end="")
    l.append(line)
f.close()

#添加名次，替换60分以下的成绩为“不及格”；
l3 = []
for i in l:
    l2 = []
    for a in i.split():
#添加名次，替换60分以下的成绩为“不及格”；
        # if a < "60":
        #     a = "不及格"
        l2.append(a)
    if l2[0] == "姓名":
        l2.insert(0,"名次")
        l2.append("总分")
        l2.append("平均分")
    
    l3.append(' '.join(l2))

# 将处理后的成绩另存为一个新文件（result.txt）    
f = open("report1.txt",'w',encoding='utf-8')
for i in l3:
    f.write(i+"\n")
    # print(i)
f.close()

 