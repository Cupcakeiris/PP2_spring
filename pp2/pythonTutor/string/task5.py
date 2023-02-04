s = input()
first = last = -1
for i in range(len(s)):
    if s[i] == 'f':
        first = i
        break

for i in reversed(range(len(s))):
    if s[i] == 'f':
        last = i
        break

if first == -1:
    print()
elif first == last:
    print(first)
else:
    print(first, last)