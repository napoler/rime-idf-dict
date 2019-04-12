#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import math
import re
import datetime
import sys, getopt
#转拼音
from pypinyin import pinyin, lazy_pinyin, Style
from segmenter import segment

class MyDocuments(object):    # memory efficient data streaming
    def __init__(self, dirname):
        self.dirname = dirname
        if not os.path.isdir(dirname):
            print(dirname, '- not a directory!')
            sys.exit()

    def __iter__(self):
        for dirfile in os.walk(self.dirname):
            for fname in dirfile[2]:
                text = open(os.path.join(dirfile[0], fname),
                            'r', encoding='utf-8', errors='ignore').read()
                yield segment(text)   # time consuming


def main(argv):   # idf generator
    inputdir = ''
    outputfile = ''

    usage = 'usage: python gen_idf.py -i <inputdir> -o <outputfile>'
    if len(argv) < 4:
        print(usage)
        sys.exit()
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["idir=","ofile="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:   # parsing arguments
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-i", "--idir"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    documents = MyDocuments(inputdir)

    ignored = {'', ' ', '', '。', '：', '，', '）', '（', '！', '?', '”', '“'}
    id_freq = {}
    i = 0
    for doc in documents:
        doc = set(x for x in doc if x not in ignored)
        for x in doc:
            id_freq[x] = id_freq.get(x, 0) + 1
        if i % 1000 == 0:
            print('Documents processed: ', i, ', time: ',
                datetime.datetime.now())
        i += 1


    # open(outputfile, 'w', encoding='utf-8')
    with open(outputfile, 'w', encoding='utf-8') as f:
        for key, value in id_freq.items():
            # if isinstance(key,str):
            #   print ("d is str")
            # print('key',key)
            # k='你是谁'
            # if isinstance(k,str):
            #   print ("k is str")
            print('key',key)
            print('value',value)
            #加入拼音
            
            # 启用多音字模式
            # k=pinyin(key,style=Style.NORMAL, heteronym=False)
            # print(pinyin(k , style=Style.NORMAL, heteronym=False))

            items=pinyin(key,style=Style.NORMAL, heteronym=False)

            #删除最后一个拼音做预测词库


            print('长度',len(items))
            new=items
            for n in range(len(items)-2):  # 启用多音字模式
                print('n',n)
                print(new)
                text_pinyin=''
                for item in new:  # 启用多音字模式
                    print(item[0])
                    text_pinyin=text_pinyin+' '+item[0]
                # print(text_pinyin)
                f.write(key + '	'+text_pinyin+'	' + str(math.log(i / value, 2)) + '\n')

                del(new[-1])


            text_pinyin=''
            for item in items:
                print(item[0])
                text_pinyin=text_pinyin+' '+item[0]

                # if isinstance(item,list):
                #     print ("b is list")
                #     for i in item:
                #         print(i)
            print(text_pinyin)
            f.write(key + '	'+text_pinyin+'	' + str(math.log(i / value, 2)) + '\n')
            # #f.write(key + '		' + str(math.log(i / value, 2)) + '\n')


if __name__ == "__main__":
   main(sys.argv[1:])
