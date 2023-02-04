s = input()
start = s.find("h")
end = s[::-1].find("h")
end = len(s) - end

rev = ''
for i in range(start+1, end-1):
    if s[i] == 'h':
        rev += s[i].upper()
    else:
        rev += s[i]

print(s[:start+1] + rev + s[end-1:])