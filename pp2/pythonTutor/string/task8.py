s = input()
start = s.find("h")
end = s[::-1].find("h")
end = len(s) - end

rev = ''
for i in range(start+1, end):
    rev += s[i]

print(s[:start] + rev[::-1] + s[end-1:])