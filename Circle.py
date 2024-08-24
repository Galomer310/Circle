
class Circle():
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("please provide a radius or diameter")

    pai = 3.14

    def radius(self):
        return self.radius

    def diameter(self):
        return self.radius * 2

    def area(self):
        area_of_circle = self.radius ** 2 * Circle.pai
        return f"Circle Area is {area_of_circle}"

    def __str__(self):
        return f"the radius of the circle is :{self.radius}, the diameter :{self.diameter()}, and the area :{self.area()}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle) and self.radius > other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Circle) and self.radius == other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented


circle1 = Circle(4)
circle2 = Circle(3)
circle3 = circle2 + circle1

print(circle1.area())
print(str(circle1))
print(circle3)
print(circle1.__lt__(circle2))
print(circle1.__eq__(circle2))

circle_list = [circle1, circle2, circle3]
circle_list.sort()

print(circle1.__gt__(circle2))
print(f"Sorted circles: {circle_list}")