from datetime import timedelta, date

yest = date.today() - timedelta(days=1)
todo = date.today()
tomo = date.today() + timedelta(days=1)
print(yest)
print(todo)
print(tomo)