import time
import sys

def rootDelay(x, t):
    # time.sleep(t/1000)
    for i in range(101):
        time.sleep(t/1000/100)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print()
    return x**(1/2)

x = 225
t = 2500 #2.5s
print(rootDelay(x, t))