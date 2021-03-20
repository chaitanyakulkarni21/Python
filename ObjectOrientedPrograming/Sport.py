class Sport:
  def __init__(self,sportName, sportType):
    self.sportName = sportName
    self.sportType = sportType

  def getSport(self):
    self.sportName = input("Enter Sport Name: ")
    self.sportType = input("Enter Sport Type: ")

  def printSport(self):
    print("Sport Name: ",self.sportName)
    print("Sport Type: ",self.sportType)

sportName = input("Enter Sport Name: ")
sportType = input("Enter Sport Type: ")
s = Sport(sportName,sportType)
#s.getSport()
s.printSport()
