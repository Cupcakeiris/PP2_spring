import math

n = int(input("Number of sides: "))
l = int(input("Length of a side: "))

p = n*l
a = l/(2 * math.tan(math.pi/n))
area = p*a/2

print(round(area))