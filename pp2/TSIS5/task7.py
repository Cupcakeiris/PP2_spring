import re
import codecs

with codecs.open("C:\KBTU\\2nd semester\pp2\TSIS5\\row.txt", encoding='utf-8') as f:
    x = []
    for line in f:
        temp = re.sub("_([а-яА-Я])", lambda l: l.group(0).upper(), line)
        if(temp): x.append(temp)

print(x)