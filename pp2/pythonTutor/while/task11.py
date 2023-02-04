s = int(input())
i = 0
prev = s
while s != 0:
    s = int(input())
    if s > prev:
        i += 1
print(i)