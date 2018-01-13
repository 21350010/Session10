

class Student():

    def __init__(self,firstName,lastName,studentNo,course):
        self.first=firstName
        self.last=lastName
        self.stdno=studentNo
        self.course=course

    def getfirst(self):
        return self.first

    def getlast(self):
        return self.last
  
    def getstdno(self):
        return self.stdno

    def getcourse(self):
        return self.course

    def setfirst(self,firstName):
        self.first=firstName

    def setlast(self,lastName):
        self.last=lastName
  
    def setstdno(self,studentNo):
        self.stdno=studentNo

    def setcourse(self,course):
        self.course=course

    def studentInfo(self):
        print(self.first,self.last,self.stdno,self.course)



def main():
    firstName = input("Enter first name :")
    lastName = input("Enter last name : ")
    studentNo = int(input("Enter student no. :"))
    course = input("Enter the course :")

    std = Student (firstName,lastName,studentNo,course)
    std.studentInfo()
    changelast = input("Enter new name : ")
    std.setlast(changelast)
    print(std.getlast())
    std.studentInfo ()

main ()                    

