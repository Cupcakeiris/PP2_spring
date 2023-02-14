class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area0 = 0
    def area(self):
        print(int(self.length) * int(self.width))

class Square(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

x = Square(input(), input())
x.area()