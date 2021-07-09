class Circle:
  pi = 3.14
  def __init__(self,radius):
    self.radius = radius

  #Instance Method
  def calculateArea(self):
    return Circle.pi*(self.radius**2)

  @classmethod
  def accesspi(cls):
    print("pi value is {}".format(Circle.pi))
  @staticmethod
  def circleStaticMethod():
    print("You are in the circle static method")

rad = int(input("Enter Radius of the circle: "))
cir = Circle(rad)
print("Area of the Circle: ",cir.calculateArea())
print("Class Method:",Circle.accesspi())
print("Static Method:",Circle.circleStaticMethod())