s = int(input())
if s % 2 == 0 and s != 0: i = 1
else: i = 0
while s != 0:
    s = int(input())
    if s % 2 == 0 and s != 0: i += 1
print(i)