import jieba
excludes = []
# 打开停用词词表文件
with open("F:/第四学期/python/py1/threekingdoms_excludes.txt","r",encoding="utf_8") as f:
    lines = f.readlines()
    print(lines)
    # 打印出lines发现每个词语后面多了\n换行符
    for line in lines:
        l = line.strip()
        # 去掉\n换行符
        excludes.append(l)
    # print(excludes)
txt = open("F:/第四学期/python/py1/threekingdoms.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
# 去掉停用词
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print("《三国演义》人物出场次数前二十：")
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))



