#Function are defined here

#Name function
def funcName(firstName,lastName):
    fName = (firstName +" "+ lastName)
    return (fName)

#Percent function

def perMarks(listMark,noSubj):
    totMark=sum(listMarks)
    marksPer = totMark/noSubj
    return marksPer


#Marks Fucntion

def totMarks(listMark):
    totMark=sum(listMarks)
    return totMark

# Grading Function

def funcGrade(marksPer):
     if(int(markPer) >= 95):
        return('A')
     elif(int(markPer) >= 85 and int(markPer) <= 95):
        return('B')
     elif(int(markPer) >= 75 and int(markPer) <= 85):
        return('C')
     elif(int(markPer) >= 65 and int(markPer) <= 75):
        return('D')
     else:
        return("FAILED")

#Master function

def masterFunc(firstName,lastName,listMarks,noSubj,marksPer):
    print(funcName(firstName,lastName))
    print("Your Percentage:", perMarks(listMarks,noSubj))
    print("Your Grade:", funcGrade(marksPer))

# Input

firstName = input("Please Enter your first name:")
lastName = input("Please Enter your last name:")
noSubj = int(input("Please enter the number of subjects"))

 #Declaring an empty list for marks
    
listMarks = []
for i in range (0,noSubj):
        markSubj = float(input("Enter the marks of subject:"))
        listMarks.append(markSubj)
marksPer = perMarks(listMarks,noSubj)

#Printing
masterFunc(firstName,lastName,listMarks,noSubj,marksPer)
