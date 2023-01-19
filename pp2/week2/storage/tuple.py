# tuple == unchangable list
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple") # NOT a tuple
print(type(thistuple))
#-------------------------
x = ("apple", "banana", "cherry")
y = list(x) # to modify tuple conver it to list
y[1] = "kiwi"
x = tuple(y)
print(x)
#-------------------------
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y # joining tuples
print(thistuple)
# del thistuple - same logic
#-------------------------
