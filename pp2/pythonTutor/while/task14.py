x = [0 , 1]
i = 2
n = int(input())
while i <= n:
    x.append(x[i-1] + x[i-2])
    i += 1
    
if(n == 0):
    print("0")
else:
    print(x[-1])