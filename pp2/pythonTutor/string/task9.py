s = input()
s = list(s)

for i in range(len(s)):
    if s[i] == '1':
        del s[i]
        s.insert(i, 'one')

for i in range(len(s)):
    print(s[i], end="")