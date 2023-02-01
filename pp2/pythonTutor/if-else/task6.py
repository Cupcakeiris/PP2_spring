repeat = 0
a = int(input())
b = int(input())
c = int(input())

if a==b: repeat +=1
if a==c: repeat +=1
if b==c: repeat +=1

if repeat == 1:
    print(repeat + 1)
else:
    print(repeat)