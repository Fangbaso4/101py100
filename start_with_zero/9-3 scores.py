# -*- utf-8 -*-
import pandas as pd

# with open('report.txt','r',encoding='utf-8') as f:
#     global scores
#     scores = [score.strip() for score in f if f]
 # print(scores)

# t1 = pd.read_table('report.txt')
# print(t1)
df1 = pd.read_csv('report.txt',header=0,sep=' ')
# print('生成dataframe:\n',df1)
# print(df1.head())
df2 = df1.loc[:,~df1.columns.isin(["index","姓名"])]
# print(df2.head())

# for index,row in df1.iterrows()
for index,col in df2.iteritems():
    print(type(df2[index]))


"""
遍历pandas行数据并进行格式化处理
"""
def format_rows(df):
    new_rw_results = []
    columns = df.columns
    for inx, rw in df.iterrows():
        for col in columns:
            new_rws = [hq_zw_zm_sz(rw[col]) for col in columns]
        new_rw_results.append(new_rws)
    new_df = pd.DataFrame(new_rw_results, columns=columns)
    return new_df