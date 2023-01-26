thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#---------------------------
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#---------------------------

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)

#---------------------------
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#---------------------------
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#---------------------------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#---------------------------
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#---------------------------
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#---------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#---------------------------
newlist = [x for x in range(10) if x < 5]

print(newlist)

#---------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

#---------------------------
thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)
#---------------------------
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#---------------------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
