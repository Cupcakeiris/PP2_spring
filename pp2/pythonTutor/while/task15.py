x = [0 , 1]
i = 2
n = int(input())
while i <= n:
    x.append(x[i-1] + x[i-2])
    i += 1
    
found = False
i = 0
while i < len(x):
    if x[i] == n:
        print(i) 
        found = True
        break
    i += 1

if not found:
    print("-1")

