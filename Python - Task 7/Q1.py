class Student:
    def __init__(self):
        self.__rollNum = 0
        self.__clgName = ""
        self.__brnchName = ""
        self.__nameFull = ""
        self.__marksList = []
        self.__totalMark = 0
        self.__perMrk = 0
        self.__stdGrade = ""

    def setStudent(self):
        self.__nameFull = input("Enter Name: ")
        self.__rollNum = input("Enter Roll: ")
        self.__clgName = input("Enter College Name:")
        self.__brnchName = input("Enter your Branch:")
        print("Enter marks of 5 subjects: ")
        for i in range(5):
            self.__marksList.append(int(input("Enter Subject "+str(i+1)+": ")))

    def funcTotal(self):
        for sumMarks in self.__marksList:
            self.__totalMark = self.__totalMark + sumMarks

    def funcPercentage(self):
        self.__perMrk = self.__totalMark/5

    def funcGrade(self):
        if self.__perMrk >= 85:
            self.__stdgrade = "S"
        elif self.__perMrk >= 75:
            self.__stdgrade = "A"
        elif self.__perMrk >= 65:
            self.__stdgrade = "B"
        elif self.__perMrk >= 55:
            self.__stdgrade = "C"
        elif self.__perMrk >= 50:
            self.__stdgrade = "D"
        else:
            self.__stdgrade = "F"



    def showStudent(self):
        self.funcTotal()
        self.funcPercentage()
        self.funcGrade()
        print("Name:" + self.__nameFull,"Roll Number:" + self.__rollNum)
        print("College Name:" + self.__clgName,"Branch Name:" + self.__brnchName)
        print("Total Marks", self.__totalMark,"Percentage:", self.__perMrk,"Your Grade:" , self.__stdgrade)


def main():
    #Student object
    stdObj=Student()
    stdObj.setStudent()
    stdObj.showStudent()

if __name__=="__main__":
    main()