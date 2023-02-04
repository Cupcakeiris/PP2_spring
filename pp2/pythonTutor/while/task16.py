s = int(input())
lst = [s]
while s != 0:
    s = int(input())
    lst.append(s)

lst.append(-1) # last element is ignored
i = 0
maxi = 1
maxlst = [maxi]
while i < len(lst) - 1:
    if lst[i] == lst[i + 1]:
        maxi += 1
    else:
        maxlst.append(maxi)
        maxi = 1
    i += 1

print(max(maxlst))