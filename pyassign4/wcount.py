#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Bai Yuchen"
__pkuid__  = "1800011798"
__email__  = "1800011798@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    strlist=[]
    for i in lines:
        string_dl=i.decode().lower()
        string=' '+string_dl+' '
        replace_list=['\r\n',',','.',':','"','!','?',"'"]
        for j in replace_list:
            string=string.replace(j,' ')
        strlist=strlist+[string]               #每行字符串的list
    all_words=[]
    for i in strlist:
        all_words=all_words+i.split()     #所有单词的list
    words=list(set(all_words))            #所有出现过的单词
    countlist=[]
    for word in words:
        countlist=countlist+[all_words.count(word)]      #每个单词出现次数
    ziplist=zip(words,countlist)
    sortlist=sorted(ziplist,key=lambda i:i[1],reverse=True)     #按次数倒序排序
    dic={}
    for item in sortlist:
        dic[item[0]]=item[1]
    if int(topn)<=len(words):
        for i in range(int(topn)):
            print(sortlist[i][0]+' ',dic[sortlist[i][0]])
    else:
        for i in range(len(words)):
            print(sortlist[i][0]+' ',dic[sortlist[i][0]])
    pass

def main():
    doc = urlopen(sys.argv[1])
    lines = doc.readlines()
    topn = sys.argv[2]
    wcount(lines,topn)    



if __name__ == '__main__':
    
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    main()