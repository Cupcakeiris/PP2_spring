import re
txt = "The rain in Spain"
pattern=re.compile(txt)
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")