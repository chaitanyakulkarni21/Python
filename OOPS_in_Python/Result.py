# Program to Calculate Avg of marks obtained by a student in 5 subjects and print the result

class Result:
  marks = []
  def getMarks(self):
    for i in range(0,5):
      self.marks.append(int(input("Enter marks in subject {} : ".format(i))))
      i = i + 1
    
  def printMarks(self):
    for i in range(0,5):
      print("Marks in Subject ", i, ": ", self.marks[i]) 
      i = i + 1

  def calAvg(self):
    s = 0
    for i in range(0, len(self.marks)):
      s = s + self.marks[i]

    self.avg = s/5 

  def printAvg(self):
    print("Average Marks: {}".format(self.avg))

  def printResult(self):
    if self.avg > 80:
      print("Result: EXCELLENT")
    elif self.avg > 40 and self.avg < 60:
      print("Result: FAIR")
    else:
      print("Result: FAILED") 
 
r = Result()
studentName = input("Enter Student Name : ")
print(' ')
r.getMarks()
print(' ')
r.printMarks()

r.calAvg()
print(' ')
r.printAvg()
print(' ')
r.printResult()