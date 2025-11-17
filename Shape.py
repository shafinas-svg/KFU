from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, size):
        self.size = size
        self.title = 'Shape'
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    def info(self):
        print(self.title)

class Square(Shape):
    def __init__(self, side):
        super().__init__(side)
        self.side=side
        self.title='квардрат'
    def calculate_area(self):
        return self.side**2
    def calculate_perimeter(self):
        return self.side * 4
    def info(self):
        return self.title
    def __str__(self):
        return f'{self.title} со стороной {self.side} см'
    def __len__(self):
        return self.side * 4
    def __eq__(self, other):
        return self.side ** 2 == other.side ** 2
    

class Circle(Shape):
    def __init__(self, Radius):
        super().__init__(Radius)
        self.Radius=Radius
        self.title='Круг'
    def calculate_area(self):
        return 3.14 * self.Radius **2
    def calculate_perimeter(self):
        return self.Radius * 2 * 3.14
    def info(self):
        return self.title
    def __str__(self):
        return f'{self.title} с радиусом {self.Radius} см'
    def __len__(self):
        return int(2 * 3.14 * self.Radius)
    def __eq__(self, other):
        return 3.14 * self.Radius ** 2 == 3.14 * other.Radius ** 2

class GeometryCalculator():
    def __init__(self):
        pass
    def validate_positive(self, number):
        if number >= 0:
            return True
        else:
            return False
        
    def calculate_diagonal(self,length, width):
        return (length ** 2 + width ** 2) ** 0.5
    def is_larger(self,shape1, shape2):
        if shape1.calculate_area() > shape2.calculate_area():
            return 'shape1 '
        elif shape1.calculate_area() < shape2.calculate_area():
            return 'shape2 '
        else:
            return 'shape1 = shape2'
        
shape1 = Square(52)
shape2 = Circle(67)
calculator = GeometryCalculator()
print(shape1.calculate_area())
print(shape1.calculate_perimeter())
print(shape1.info())
print(shape2.calculate_area())
print(shape2.calculate_perimeter())
print(shape2.info())
print(calculator.validate_positive(666))
print(calculator.calculate_diagonal(22, 8))
print(calculator.is_larger(shape1, shape2))
        