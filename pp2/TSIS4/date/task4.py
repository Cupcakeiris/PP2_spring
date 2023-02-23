import datetime

x = datetime.datetime(2022, 9, 1).timestamp()
y = datetime.datetime.now().timestamp()
diff = y - x
print("Seconds since I'm studying in KBTU: ")
print(round(diff))