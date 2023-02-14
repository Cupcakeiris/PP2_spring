class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, a, b):
        self.x = a
        self.y = b

    def dist(self, x2, y2):
        d = ((self.x - x2)**2 + (self.y - y2)**2) ** (1/2)
        print(d)

print("Enter p1 coordinates: ")
p1 = Point(int(input()), int(input()))
print("Enter p2 coordinates: ")
p2 = Point(int(input()), int(input()))
print("p1 coordinates: ", end="")
p1.show()
print("p2 coordinates: ", end="")
p2.show()
print("Enter p2 new coordinates: ")
p2.move(int(input()), int(input()))
print("p2 new coordinates: ", end="")
p2.show()
print("distance between p1 and p2: ", end="")
p1.dist(p2.x, p2.y)

