from pypinyin import pinyin, lazy_pinyin, Style

key= '下存狗子'
 
text=''
items = pinyin(key,style=Style.NORMAL, heteronym=False)

print('长度',len(items))
new=items
for n in range(len(items)):  # 启用多音字模式
    print('n',n)
    print(new)
    text=''
    for item in new:  # 启用多音字模式
        print(item[0])
        text=text+' '+item[0]
    print(text)
    del(new[-1])



# del(items[-1])
# print(del(items[-1]))
# for item in items:  # 启用多音字模式
#     print(item[0])
#     text=text+' '+item[0]

#     # if isinstance(item,list):
#     #     print ("b is list")
#     #     for i in item: 
#     #         print(i)
# print(text)