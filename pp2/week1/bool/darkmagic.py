print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# these give false:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))