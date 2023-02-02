p = int(input())
x = int(input())
y = int(input())
start = 100 * x + y
total = int(start * (100 + p) / 100) # bank formula for arithemtic progression
print(total // 100, total % 100)