fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

#-----------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#-----------
for x in range(2, 30, 3):
  print(x) 

#-----------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#-----------
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement
