s = int(input())
lst = []
while s != 0:
    lst.append(s)
    s = int(input())

m = sum(lst) / len(lst)

num = 0
for i in lst:
    num += (i - m) ** 2

res = (num  / (len(lst) - 1)) ** (1/2)
print(res)

