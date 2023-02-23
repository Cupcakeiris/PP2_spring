def decGen(n):
    for i in reversed(range(0, n+1)):
        yield i

n = int(input())
gen = decGen(n)

for i in range(n):
    print(next(gen))