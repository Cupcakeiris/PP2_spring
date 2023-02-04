s = input()
s = list(s)

for i in s:
    if i == '@':
        s.remove('@')

for i in range(len(s)):
    print(s[i], end="")