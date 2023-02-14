def rever(x):
    temp = []
    for i in reversed(range(len(x))):
        temp.append(x[i])
    return temp

x = "Black cats are cute"
x = x.split(" ")
x = rever(x)
for i in x:
    print(i, end=" ")