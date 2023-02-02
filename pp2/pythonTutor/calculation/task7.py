a = int(input())
b = int(input())
n = int(input())

total = (b / 100 + a) * n
print(int(total), int((total*100)%100))
