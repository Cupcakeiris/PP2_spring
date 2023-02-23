import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
#--------------------------
#Return a list containing every occurrence of "ai":
x = re.findall("ai", txt)
print(x)
#--------------------------
#Replace all white-space characters with the digit "9":
x = re.sub("\s", "9", txt)
print(x)
#--------------------------
x = re.findall("[a-m]", txt)
print(x)
#--------------------------
#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
#--------------------------
#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#--------------------------
x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#--------------------------
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
