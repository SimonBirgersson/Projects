# fiddling around with class inheritance 220221
from statistics import mean


# parent class
class Enzyme:
  def __init__(self, abs, blank):
    self.abs = [x - mean(blank) for x in abs]
    self.conc = 

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Enzyme):
  pass
