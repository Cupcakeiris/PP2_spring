import re
import codecs

with codecs.open("C:\KBTU\\2nd semester\pp2\TSIS5\\row.txt", encoding='utf-8') as f:
    x = []
    for line in f:
        temp = re.sub(r"(\w)([А-Я])", r"\1 \2", line)
        if(temp): x.append(temp)

print(x)