# Windows下源文件都是ansi格式
# Windows下源文件都是ansi格式
'''
本程序用法：
python countfile_novary.py 源文件 结果文件
例如：
python countfile_novary.py a1.txt r1.txt

对 "源文件" 进行单词词频分析，分析结果写入 "结果文件"
如果碰到单词的变化形式，则转换成原型再统计

单词原型-变化 词汇表：word_varys.txt
格式：

act
	acted|acting|acts
action
	actions
active
	actively|activeness


'''

import sys
import re


def makeVaryWordsDict(): # 形成一个记录同形词的词典
    dict = {}
    f = open("word_varys.txt", "r")
    lines = f.readlines()  # 读完之后形成列表
    f.close()
    l = len(lines)
    for i in range(0, l, 2):
        word = lines[i].strip()
        varys = lines[i + 1].strip("|")
        for w in varys:
            dict[w] = word
    return dict

def makeSplitStr(txt): # 形成用于 re.split() 的切割字符串
    splitChars = set([])
    # 下面找出所有文件中非字母的字符，作为分隔符
    for c in txt:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z'):
            splitChars.add(c)
    splitStr = ""
    # 生成用于 re.split的分隔符字符串
    for c in splitChars:
        if c in ['.', '?', '!', '"', "'", '(', ')', '|', '*', '$', '\\', '[', ']', '^', '{', '}']:
            splitStr += "\\" + c + '|'
        else:
            splitStr += c + "|"
    splitStr += " "
    return splitStr


def countFile(filename, vary_word_dict):
    # 分析 filename 文件，返回一个词典作为结果。到 vary_word_dict里查单词原型
    try:
        f = open(filename, "r", encoding="gbk")
    except Exception as e:
        print(e)
        return None
    txt = f.read()
    f.close()
    splitStr = makeSplitStr(txt)
    words = {}
    lst = re.split(splitStr, txt)
    for x in lst:
        lx = x.lower()
        if lx == "":
            continue
        if lx in vary_word_dict:  # 如果在原型词典里能查到原型，就变成原型再统计
            lx = vary_word_dict[lx]
        # 直接写这句可以替换上面 if 语句  lx = vary_word_dict.get(lx,lx)
        words[lx] = words.get(lx, 0) + 1
    return words


result = countFile(sys.argv[1], makeVaryWordsDict())
if result != None and result != {}:
    lst = list(result.items())
    lst.sort()
    f = open(sys.argv[2], "w", encoding="gbk")
    for x in lst:
        f.write("%s\t%d\n" % (x[0], x[1]))
    f.close()
