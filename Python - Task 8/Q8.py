#Main Function


def main():
    #declaring an empty list to add objects of class Course
    courseList = []
    courseListFunc(courseList)

    #declaring an empty list to add objects of class Student
    stdList = []
    studentList(stdList, courseList)

    choice = 0
    
    while choice >= 0:
        #calling of menu()
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("--Course ID--      --Course Name--        --Course Credit--")
            
            #iterating to print the list of available courses
            for i in range(courseList.__len__()):
                Course.getCourse(courseList[i])
                print()
            print()

        if choice == 2:
            print("--Student ID--       --Student Name--")
            
            #iterating to print the list of students
            for i in range(stdList.__len__()):
                Student.dispStudent(stdList[i])
            print()

        if choice == 3:
            
            #iterating to print the list of students and their enrollement
            for i in range(stdList.__len__()):
                Student.stuEnrollment(stdList[i],0)
            print()

        if choice == 4:
		#Checking if fees is paid or not
            for i in range(stdList.__len__()):
                if stdList[i].checkFee() == True:
                    Student.stuEnrollment(stdList[i],1)
                else:
                    #if fee is not paid
                    Student.dispStudent(stdList[i])
                    print("Please pay the tuiton fees",Student.calFee(stdList[i]),"baht")
            print()

        if choice == 0:
            print("Exit")







#SuperClass person defined

class Person:
  def __init__(self):
    self.__Fname = " "
    self.__Lname = " "

  def printName(self):
    self.__Fname = input("Enter First Name:")
    self.__Lname = input("Enter Last Name:")

#Inherting the student class
    
class Student(Person):
    def __init__(self):
        super().__init__(self)
        self.__Fname = " "  
        self.__Lname = " " 
        self.__stdID = " " 
        self.__noOfCourses = ""
        self.__feePaid = " "
        self.__listCourses = " " 
        self.__listGrader = " "
    
    
   
    #function to check if fees is paid or not

    def checkFee(self):
        if(self.paidFee == 1):
            x = True
            return(bool(x))
        else:
            x = False
            return(bool(x))




    #using acceser and mutators
    
    def stdFee(self):
        tot = 0;
        for i in range (0,self.__noOfCourses):
            tot = tot + course.courseCredit(self.listCourses[i])
        return(tot * 500)
    
    
    #function to calculate and return GPA of a student
    def calGPA(self):
        sum = 0
        x = 0
        
        stdGradeList = []

        for i in range(self.__noOfCourses):
            sum += Course.crsCredit(self.__listCourses[i])

        for i in range(self.__noOfCourses) :
            if self.__listGrader[i] == "A":
                gradeW = 4
            elif self.__listGrader[i] == "B":
                gradeW = 3
            elif self.__listGrader[i] == "C":
                gradeW = 2
            elif self.__listGrader[i] == "D":
                gradeW = 1
            else:
                gradeW = 0
            stdGradeList.append(gradeW)

        for i in range(self.__noOfCourses):
            totCred += Course.crsCredit(self.__listCourses[i]) * stdGradeList[i]

      
        stdGPA = totCred / sum
        return(stdGPA)

        
    #Using Functions to display student info
    def dispStudent(self):
        print(self.studentId, end ="    ")
        Person.getPerson(self)

    def stuEnrollment(self, flag):
        print(self.studentId, end = "")
        Person.getPerson(self)
        print("--Course ID --       --Course Name--    --Course Credit Grades--")
        for i in range(self.__noOfCourses):
            Course.getCourse(self.__listCourses[i])
            print(self.__listGrader[i])
            
        tutionFee = Student.calFee(self)
        if(flag == 0):
            print("Tuition Fee:",tuitionFee,"baht")
        else:
            print("Tuition Fee paid:",tuitionFee,"baht")
        stdGPA = Student.calGPA(self)
        print("Student GPA:",stdGPA)        
    
    
    
    
class Course:
    
    #Constructor
    
    def __init__(self,__courseID,__courseName,__courseCredits):
        self.__courseName = ""
        self.__courseID = ""
        self.__courseCredits = ""
        
    #returning credits
    
    def creditCourse(self):
        return(self.__courseCredits)    
        
    #Printing the details of the student
    
    def detailCourse(self):
        print(self.__courseName)
        print(self.__courseID)
        print(self.__courseCredits)
        
    #Course menu
def courseMenu():
        
    print("***MENU***")
    print("1.List Courses")
    print("2.List Students")
    print("3.List Students and Enrollment")
    print("4.Grade Report")
    print("0.Exit")
    
    
    
def courseListFunc(courseList):
     i = 0
     while(i <= 6):
        CourseIdFunc = int(input("Enter Course ID:"))
        CourseSubFunc = input("Enter Course Name:")
        CourseCrFunc = int(input("Enter the course credits:"))
        objCrs = Course(CourseIdFunc,CourseSubFunc,CourseCrFunc)    
        courseList.append(objCrs)
        i = i+1
    
    
def studentList(stdList, courseList):
    objStu = Student(12345, "John Wayn", 4,1,[cousreList[0],cousreList[1],cousreList[5],cousreList[6]],['A','B','B','A'])
    stdList.append(objStu)
    objStu = Student(12346, "Jane March", 5,1,[cousreList[1],cousreList[2],cousreList[4],cousreList[5],cousreList[6]],['A','B','B','C','D'])
    stdList.append(objStu)
    objStu = Student(12347, "Marry Dolphin", 5,0,[cousreList[0],cousreList[3],cousreList[4],cousreList[5],cousreList[6]],['C','B','C','A','B'])
    stdList.append(objStu)    


    
#Calling the Main Function         
main()
           
        