# -*- Utf-8 -*-
'''
要求：实现一个方法，输入一段文字，将其中存在于列表中的词汇字符替换成 *，返回处理后的文字。
验证这个方法时，从控制台输入待检测文字，调用方法处理，输出处理后的文字。
如：
abcdefg -> ** *defg
啊啊，这是一个测试啊啊啊啊 -> 啊啊，这是一个 ** ** *啊
主要涉及内容：文件读取、字符串处理、函数调用
'''
#获取屏蔽词
with open('8-9 words.txt','r',encoding='utf-8') as f:
    global blockedWords
    blockedWords = [line.strip() for line in f ]
    #blocked_words = [l.strip() for l in f.readlines() if l]
    # 这里是为了去掉读进来的内容中带有的空格、换行符、空字符等，等同于以下代码
    # blocked_words = []
    # lines = f.readlines()
    # for l in lines:
    #     if l:  # 如果 l 不为空，即去掉空行
    #         l = l.strip()  # 去除字符前后的空格和回车
    #         blocked_words.append(l)
print(blockedWords)
#进行屏蔽词替换
def wordsReplace(words,Rword='*'):
    for word in blockedWords:
        words = words.replace(word,Rword * len(word))
    return words
text = '啊啊，这是一个测试啊啊啊啊'
# print(wordsReplace(text))

# 【解决思路】
# 首先从文件中读取屏蔽词列表，并保存在变量中。一次运行只需读取一次即可，不用每次匹配时都去读一遍。
# 读取后的数据要保证不含有空格、换行符、空行等，以免干扰正常匹配。所以，如果是按行读入，要判断读进来的是否是一个空行，然后再把字符前后的换行符给去掉（通常用 str 的 strip 方法）
# 比较直接的匹配方法就是，遍历屏蔽词列表中的每个词，然后从待检测字符中将其替换掉（如果存在的话），可以用 str 的 replace 实现。
# 附加题1：示例中如果英文屏蔽词和输入字符的大小写不匹配，是无法替换掉的。如何既能忽略大小写进行屏蔽，又能保证其他字母的大小写正常？（提示：需要手动增加大小写转换）
# 附加题2：如果“仙人”是屏蔽词，则会把“仙人掌”误判为“**掌”。想减少误判率，可使用分词库改进方法，最常用的中文分词库是 jieba 分词库。
import jieba
jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]
for text in strs:
    seg_list = jieba.cut(text, cut_all=True)
    print(','.join(seg_list))
    # print("Full Mode: " + "/ ".join(seg_list))  # 全模式