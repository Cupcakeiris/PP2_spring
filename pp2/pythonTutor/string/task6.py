s = input()
f = -1

start = s.find('f')
if start == -1:
    f = -2

for i in range(start+1, len(s)):
    if s[i] == 'f':
        f = i
        break

print(f)