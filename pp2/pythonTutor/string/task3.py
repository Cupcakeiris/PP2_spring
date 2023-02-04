import math
s = input()
half = math.ceil(len(s) / 2)

s1 = s[:half]
s2 = s[half:]

print(s2 + s1)