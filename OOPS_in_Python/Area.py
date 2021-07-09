class Rectangle:
  def __init__(self, length, breadth):
    self.length = int(length)
    self.breadth = int(breadth)

  def calArea(self):
    return self.length*self.breadth
  
  def calPerimeter(self):
    return 2*(self.length+self.breadth)

l,b = input("enter length and breadth of the rectangle : ").split()
print("Length:",l, "and Breadth: ",b)
rect = Rectangle(l,b)
print("Area of the rectangle = ", rect.calArea())
print("Perimeter of the Rectangle = ", rect.calPerimeter())
