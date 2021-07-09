from typing import Coroutine


class Shape:
  def set_color(self,color):
    self.color = color
  def calculateArea(self):
    pass
  def color_the_shape(self):
    color_price = {'red':10,'blue':15,'green':5}
    return self.calculateArea() * color_price(self.color)

class Circle(Shape):
  pi = 3.14
  def __init__(self,radius):
    self.radius = radius

  def calculateArea(self):
      return Circle.pi * self.radius**2

rad = int(input("Enter radius of the circle:"))
c = Circle(rad)
c_color = input("Enter circle color:")
c.set_color(c_color)
print("Radius:",c.radius,"Area:",c.calculateArea(),"Color:",c.color, "Value of Pi:",c.pi, "Color the Shape:",c.color_the_shape())

class Rectangle(Shape):
  def __init__(self,length, breadth):
    self.length = length
    self.breadth = breadth
  def calculateArea(self):
    return self.length * self.breadth

l,b = map(int, input("Enter the length and breadth of the rectangle: ").split())
r = Rectangle(l,b)
r_color = input("Enter rectangle color: ")
r.set_color(r_color)
print("Length: ",r.length, "Breadth:",r.breadth, "Area:",r.calculateArea(), "Color:",r.color, "Color the shape:",r.color_the_shape())