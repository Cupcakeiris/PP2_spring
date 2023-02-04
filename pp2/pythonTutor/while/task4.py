x = int(input())
y = int(input())
i = 1
while x<=y:
    if x==y:
        break
    x += y/10
    i += 1

print(i)