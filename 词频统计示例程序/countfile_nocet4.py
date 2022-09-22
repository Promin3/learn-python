# Windows下源文件都是ansi格式
# Windows下源文件都是ansi格式
'''
本程序用法：
python countfile_nocet4.py 源文件 结果文件
例如：
python countfile_nocet4.py a1.txt r1.txt

对 "源文件" 进行单词词频分析，只抽取不在四级单词列表中的单词，将分析结果写入 "结果文件"

四级单词列表： cet4words.txt
其格式：

$abandon
[?'b?nd?n]
vt.遗弃；放弃；放纵(自己)
$ability
[?'b?l?t?]
n.能力，才能
$able
['e?bl]
a.有的能力；有本事的，能干的
$aboard
[?'b?:d]
ad.&prep.在船(飞机、车)上；ad.上船(飞机)

....

'''
import sys
import re


def makeFilterSet():
    cet4words = set([])
    f = open("cet4words.txt", "r", encoding="gbk")
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line[0] == "$":
            cet4words.add(line[1:])  # 将四级单词加入 集合
    return cet4words


def makeSplitStr(txt):
    splitChars = set([])
    # 下面找出所有文件中非字母的字符，作为分隔符
    for c in txt:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z'):
            splitChars.add(c)
    splitStr = ""
    # 生成用于 re.split的分隔符字符串
    for c in splitChars:
        if c in ['.', '?', '!', '"', "'", '(', ')', '|', '*', '$', '\\', '[', ']', '^', '{', '}']:
            splitStr += "\\" + c + "|"
        else:
            splitStr += c + "|"
    splitStr += " "
    return splitStr


def countFile(filename, filterdict):  # 词频统计，要去掉在 filterdict集合里的单词
    words = {}
    try:
        f = open(filename, "r", encoding="gbk")
    except Exception as e:
        print(e)
        return 0
    txt = f.read()
    f.close()
    splitStr = makeSplitStr(txt)
    lst = re.split(splitStr, txt)
    for x in lst:
        lx = x.lower()
        if lx == "" or lx in filterdict:  # 去掉在 filterdict里的单词
            continue
        words[lx] = words.get(lx, 0) + 1
    return words





result = countFile(sys.argv[1], makeFilterSet())
if result != {}:
    lst = list(result.items())
    lst.sort()
    f = open(sys.argv[2], "w", encoding="gbk")
    for x in lst:
        f.write("%s\t%d\n" % (x[0], x[1]))
    f.close()
