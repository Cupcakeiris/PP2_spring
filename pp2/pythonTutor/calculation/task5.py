a = int(input())
time = 0
for i in range(1, a+1):
        
    time += 45
    if i%2==0:
        time += 15
    else:
        time += 5


h = int(time / 60) % 24
m = time % 60

if a%2 == 0:
    m -= 15
else:
    m -= 5

print(h + 9, m)