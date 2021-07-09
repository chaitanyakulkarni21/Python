class Vehicle:
    def __init__(self, modelName, year, regNo):
        self.modelName = modelName
        self.year = year
        self.regNo = regNo

    def vehicleInfo(self):
        print(' ')
        print("Vehicle Model Name: ", self.modelName)
        print("Vehicle Registration number: ", self.regNo)
        print("Vehicle was purchased in Year?: ", self.year)


model = input("Enter vehicle model name : ")
reg = input("Enter vehicle registration number: ")
year = input("When was the vehicle purchased ? : ")

vh = Vehicle(model, year, reg)
vh.vehicleInfo()
