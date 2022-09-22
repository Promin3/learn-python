'''
本程序用法：
python countfiles.py 结果文件
例如：
python countfiles.py result.txt

对当前文件夹下全部 "a*.txt"文件进行词频分析，分析的总的结果写入  "结果文件"

'''
import sys
import re
import os


def countFile(filename, words):
    # 对 filename 文件进行词频分析，分析结果记在词典 words里
    try:
        f = open(filename, "r", encoding="gbk")  # 文件为缺省编码。根据实际情况可以加参数 encoding="utf-8" 或 encoding = "gbk"
    except Exception as e:
        print(e)
        return 0
    txt = f.read()  # 全部文件内容存入字符串txt
    f.close()
    splitChars = set([])  # 分隔串的集合
    # 下面找出所有文件中非字母的字符，作为分隔串
    for c in txt:
        if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
            continue
        splitChars.add(c)
    splitStr = ""  # 用于 re.split的正则表达式
    # 该正则表达式形式类似于： ",|:| |-" 之类，两个竖线之间的字符串就是分隔符
    for c in splitChars:
        if c in {'.', '?', '!', '"', "'", '(', ')', '|', '*', '$', '\\', '[', ']', '^', '{', '}'}:
            # 上面这些字符比较特殊，加到splitChars里面的时候要在前面加 "\"
            splitStr += "\\" + c + "|"  # python字符串里面，\\其实就是  \
        else:
            splitStr += c + "|"
    splitStr += " "  # '|'后面必须要有东西，空格多写一遍没关系
    lst = re.split(splitStr, txt)  # lst是分隔后的单词列表
    for x in lst:
        if x == "":  # 两个相邻分隔串之间会分割出来一个空串，不理它
            continue
        lx = x.lower()
        if lx in words:
            words[lx] += 1  # 如果在词典里，则改词出现次数+1
        else:
            words[lx] = 1  # 如果不在词典里，则将该词加入词典，出现次数设为1
    return 1


result = {}  # 结果字典
lst = os.listdir()  # 列出当前文件夹下所有文件和文件夹
for x in lst:
    if os.path.isfile(x):  # 如果x是文件
        if x.lower().endswith(".txt") and x.lower().startswith("a"):
            # x是 'a'开头， .txt结尾
            countFile(x, result)
lst = list(result.items())
lst.sort()  # 单词按字典序排序
f = open(sys.argv[1], "w", encoding="gbk")  # argv[2] 是结果文件, 文件为缺省编码, "w"表示写入
for x in lst:
    f.write("%s\t%d\n" % (x[0], x[1]))
f.close()
