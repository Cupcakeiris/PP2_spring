import math
h = int(input())
a = int(input())
b = int(input())

# a * x - b * (x - 1) = h
# a * x - b * x + b = h
# x(a - b) = h - b
# x = (h - b)/(a - b)

print(math.ceil((h - b)/(a - b)))