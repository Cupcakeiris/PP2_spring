f = open("C:\KBTU\\2nd semester\pp2\w3schools\week6\demo.txt", "r")
#----------------------
print(f.read(5))
#----------------------
print(f.readline())
#----------------------
for x in f:
  print(x)

f.close()
#----------------------
f = open("C:\KBTU\\2nd semester\pp2\w3schools\week6\demo.txt", "a")

f.write("Now the file has more content!")
#----------------------
# f = open("C:\KBTU\\2nd semester\pp2\w3schools\week6\\newdemo.txt", "x")
f = open("C:\KBTU\\2nd semester\pp2\w3schools\week6\\newdemo.txt", "w")

f.write("Woops! I have deleted the content!")
f.close()
#----------------------
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#----------------------
os.rmdir("C:\\KBTU\\2nd semester\\pp2\\w3schools\\week6\\unused_folder")