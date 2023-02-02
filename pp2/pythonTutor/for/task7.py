sum = 1
total = 0
n = int(input())

for i in range(1, n+1):
    sum *= i
    total += sum
print(total)