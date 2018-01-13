
class Student():

    def __init__(self,FirstName,LastName,StudentNo,Course):
        self.first=FirstName
        self.last=LastName
        self.stdno=StudentNo
        self.course=Course

    def getfirst(self):
        return self.first

    def getlast(self):
        return self.last
  
    def getstdno(self):
        return self.stdno

    def getcourse(self):
        return self.course

    def setfirst(self,FirstNameinput):
        self.first=Firstname

    def setlast(self,LastNameinput):
        self.last=lastinput
  
    def setstdno(self,StudentNoinput):
        self.stdno=stdnoinput

    def setcourse(self,Courseinput):
        self.course=courseinput

    def studentInfo(self):
        print(self.first,self.last,self.stdno,self.course)
        
std_1=Student("John","Baker",4321,"IT")
std_2=Student("Daniel","Smith",4322,"Law")
std_3=Student("Andrew","Coward",4323,"Management")
        
std_1.studentInfo()
std_2.studentInfo()
std_3.studentInfo()

