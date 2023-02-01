a = int(input())
b = int(input())
x = int(input())
y = int(input())

if (abs(a-x)) == (abs(b-y)):
    print("YES")
elif a == x or b == y:
    print("YES")
else:
    print("NO")