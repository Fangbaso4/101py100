'''
读取 report.txt 文件中的成绩；
统计每名学生总成绩、计算平均并从高到低重新排名；
汇总每一科目的平均分和总平均分（见下表第一行）；
添加名次，替换60分以下的成绩为“不及格”；
将处理后的成绩另存为一个新文件（result.txt）。
'''

#读取 report.txt 文件中的成绩；
with open("report.txt","r",encoding="utf-8") as f:
    record = [line.strip() for line in f]
    # print(record) 
    # print(len(record))

def takeLastSecond(elem):
    return elem[-1]
#统计每名学生总成绩、计算平均并从高到低重新排名；
score = []
result = []
for num in range(len(record)):
    if num > 0:
        AvgScore = 0
        SumScore = 0
        score = record[num].split()
        for numS in range(len(score)):
            if numS > 0:
                SumScore = SumScore + int(score[numS])
            AvgScore = SumScore/(len(score)-1)
        score.append(str(SumScore))
        score.append(str(round(AvgScore,1)))
    else :
        score = record[num].split()
        score.append("总分")
        score.append("平均分")
    # score = ' '.join(score)
    result.append(score)
# print(len(result))
scores = result[0:1]+ sorted(result[1:],key=takeLastSecond,reverse=True)
# print(len(scores))

#计算每一学科的平均值
def flaten(array):
    for item in array:
        if isinstance(item, list):
            yield from flaten(item)
        else:
            yield item

avgsubj = []
for i in range(len(score)):
    subject = []
    if i == 11:
        subject = list(flaten(scores))[i::12]
        sumsubj = 0
        for j in range(len(subject)):
            if j > 0:
                sumsubj = sumsubj + float(subject[j])
        avgsubj.append(str(round(sumsubj/(len(subject)-1),1)))
    elif i > 0 :
        subject = list(flaten(scores))[i::12]
        sumsubj = 0
        for j in range(len(subject)):
            if j > 0:
                sumsubj = sumsubj + int(subject[j])
                # 替换不及格分数
                if int(scores[j][i]) <60:
                    scores[j].insert(i,"不及格")
                    del scores[j][i+1]
        avgsubj.append(str(round(sumsubj/(len(subject)-1))))
    else :
        avgsubj.append('平均')
    # print(subject)
# print(avgsubj)
scores.insert(1,avgsubj)
# print(scores)

#添加名次
listscore = []
for i in range(len(scores)):
    if i > 0:
        scores[i].insert(0,str(i-1))
    else :
        scores[i].insert(0,"名次")
    listscore.append(' '.join(scores[i]))
# print(listscore)



# 将处理后的成绩另存为一个新文件（result.txt）    
f = open("report2.txt",'w',encoding='utf-8')
for i in range(len(listscore)):
    f.write(''.join(str(listscore[i]))+"\n")
    # print(i)
f.close()
