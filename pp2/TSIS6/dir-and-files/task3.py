import os

path = "C:\KBTU\\2nd semester\pp2\\task.py"

print(os.path.exists(path))
directory = os.getcwd()
portion = directory.split("\\")
print(portion[-1])