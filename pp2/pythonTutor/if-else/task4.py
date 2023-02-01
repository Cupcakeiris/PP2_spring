y = int(input())

if y % 4 == 0:
    if y % 100 == 0:
        print("NO")
    elif y % 400:
        print("YES")
else:
    print("NO")