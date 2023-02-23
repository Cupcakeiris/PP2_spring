import os

path = "C:\KBTU\\2nd semester\pp2"

print(os.path.exists(path))

if os.access(path, os.R_OK):
    print("You can access")
else:
    print("No access")

if os.access(path, os.W_OK):
    print("You can write")
else:
    print("No writing")

if os.access(path, os.X_OK):
    print("You can execute")
else:
    print("No executing")   