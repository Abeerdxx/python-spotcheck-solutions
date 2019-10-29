class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2*self.width + 2*self.height

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def calculate_perimeter(self):
        return self.length * 4

s = Square(2)

print(s.calculate_perimeter()) # outputs: 8
print(s.calculate_area()) # outputs: 4