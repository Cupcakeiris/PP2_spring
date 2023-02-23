n = int(input())
lst = [x**2 for x in range(1, n+1)]
gen = iter(lst)

for i in gen:
    print(i)