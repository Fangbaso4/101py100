# -*- utf-8 -*-
#要求：输入关键字，列出指定文件夹中的所有文件名中含有此关键字的文件/目录，以及文件内容中含有此关键字的文件。
import os
def findFile(keyword,inputdir = '.'):
    fileList = []
    fileName = [file for file in os.listdir() if keyword in file ]
    print(fileName)

keyword = input('输入需要查询的关键字：')
inputdir = input('查询路径（为空默认程序当前目录）：')
dirconf = os.path.isdir(inputdir)
while dirconf == False:
    inputdir = input('请输入正确查询路径（为空默认程序当前目录）：')
    dirconf = os.path.isdir(inputdir)

findFile(keyword,inputdir)
# findFile('data')
