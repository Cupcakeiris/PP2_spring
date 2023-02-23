def squaresGen(n):
    for i in range(1, n):
        yield i ** 2
    yield n ** 2

n = int(input())
gen = squaresGen(n)

for i in range(n):
    print(next(gen))