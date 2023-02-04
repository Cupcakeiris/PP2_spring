s = int(input())
lst = []
while s != 0:
    s = int(input())
    lst.append(s)

max = max(lst)

i = 0
maxi = 0
while i < len(lst):
    if lst[i] == max: maxi += 1
    i += 1
print(maxi)