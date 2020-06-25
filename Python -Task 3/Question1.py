#Function are defined here
#Name function
def funcName():
    firstName = input("Please Enter your first name:")
    lastName = input("Please Enter your last name:")
    fName = firstName +" "+ lastName)
    return (fName)
#Marks Fucntion

def funcMarks(noSubj):
    #Declaring an empty list for marks
    listMarks = []
    for i in range (0,noSubj):
            markSubj = float(input("Enter the marks of subject"))
            listMarks.append(markSubj)
    tot=sum(listMarks)
    return tot
    
noSubj = int(input("Enter the number of subjects:"))

#Function for grades

def funcGrade(noSubj,tot):
    marksPer = tot/noSubj
    print("Your Percentage is:",marksPer)
    return (marksPer)
Percenatge = funcGrade(noSubj,funcMarks(noSubj))   

#Function for grades
def funcGrade(markPer):
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

# function to call all the functions
def masterFunc(markPer,percentage):
    print("The Grade of the student is",funcGrade(markPer))
    print("The percentage of studrnt is",percentage )
    print("The name of student is"Fname)

    # Calling the function
masterFunc(markPer,percentage,Name)
    