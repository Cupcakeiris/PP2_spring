thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#---------------------
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#---------------------
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#---------------------
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#---------------------
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#---------------------

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#---------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)

#---------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)

