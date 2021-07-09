class A :
    x = 10
    def __init__(self, y,z):
        self.y = y
        self.z = z
           
    def update_y(self):
        self.y = self.y * self.x
        self.z = self.z * self.x
        
A1 = A(3,4)
A2 = A(5,6)

A1.update_y()
print(A1.y + A2.z)