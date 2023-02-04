s = int(input())
max = s
maxi = 1
i = 1
while s != 0:
    s = int(input())
    i += 1
    if s > max:
        max = s
        maxi = i

print(maxi)