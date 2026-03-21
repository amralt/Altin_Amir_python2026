class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height*self.width
    
    def perimetr(self):
        return (self.height + self.width)*2
    
    def __eq__(self, other: Rectangle):
        return self.area() == other.area()
    
    def __lt__(self, other: Rectangle):
        return self.area() < other.area()
    
    def __add__(self, other: Rectangle):
        if (self.width == other.width):
            return Rectangle(self.width, self.height + other.height)
        if (self.width == other.height):
            return Rectangle(self.width, self.height + other.width)
        if (self.height == other.width):
            return Rectangle(self.height, self.width + other.height)
        if (self.height == self.height):
            return Rectangle(self.height, self.width + other.width)
        
        raise Exception("Не получилось склеить")

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __str__(self):
        return f"Прямоугольник {self.width}*{self.height}"
    
rec1 = Rectangle(3,4)
print(rec1)
print(rec1.area())

rec2 = Rectangle(7, 4)
print(f"eq {rec1 == rec2}")
print(f"lt {rec1 < rec2}")

rec3 = rec1 + rec2
print([rec3])
print(rec3)
