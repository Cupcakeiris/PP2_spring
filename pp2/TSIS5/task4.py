import re
import codecs

with codecs.open("C:\KBTU\\2nd semester\pp2\TSIS5\\row.txt", encoding='utf-8') as f:
    x = []
    for line in f:
        temp = re.findall(r"^[А-Я]+[а-я]+", line)
        if(temp): x.append(temp)

print(x)