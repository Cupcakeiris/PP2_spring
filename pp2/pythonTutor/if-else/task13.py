n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n > m:
    max = n
    min = m
else:
    max = m
    min = n

if x >= min / 2:
    x = min - x
if y >= max / 2:
    y = max - y

if x < y:
    print(x)
else:
    print(y)