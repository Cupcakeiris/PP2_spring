class Shape:
    def __init__(self, length):
        self.length = length
        self.area0 = 0
    def area(self):
        print(int(self.length) ** 2)

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

x = Square(input())
x.area()