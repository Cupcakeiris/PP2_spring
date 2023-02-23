import datetime

x = datetime.datetime.now()

print(x)
#-------------------------
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#-------------------------
x = datetime.datetime(2020, 5, 17)

print(x)
#-------------------------
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
#-------------------------
x = datetime.datetime.now()

print(x.strftime("%p"))
#-------------------------
x = datetime.datetime.now()

print(x.strftime("%f"))
#-------------------------
x = datetime.datetime.now()

print(x.strftime("%c"))
#-------------------------
x = datetime.datetime.now()

print(x.strftime("%%"))
