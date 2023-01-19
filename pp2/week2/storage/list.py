# list == vector
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
thislist.insert(1, "pear")
print(thislist)
#--------------------------
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) # extend works for all data storage typess
print(thislist) 
#--------------------------
thislist.pop(0)
thislist.remove("kiwi")
del thislist[0]
print(thislist)
#--------------------------
thislist.clear()
print(thislist) # clears all element of list
del thislist # deletes list itself
#--------------------------
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # comprehension takes less space than traditional way
#--------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "apple" != x] # without if it copies all elements
newlist.sort(reverse=True)
print(newlist)
#--------------------------
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # own logic to sort
print(thislist)
#--------------------------
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # another ways to copy
mylist = list(thislist)
print(mylist)
#--------------------------
list1 = ["a", "b"]
list2 = [1, 2]
list3 = list1 + list2 # or with for loop and append, extend
print(list3)
