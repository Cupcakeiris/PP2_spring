s = int(input())
max1 = s
max2 = s
while s != 0:
    s = int(input())
    if s > max1:
        max2 = max1
        max1 = s
    elif s > max2:
        max2 = s
print(max2)