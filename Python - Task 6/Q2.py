#Question 2
#Function for
def emList(nonemList):
    nonemList = [emList for emList in nonemList if emList]
    print("Non Empty list is",nonemList)

#Declaring list
finList = []
line = input("Enter the list of tuples:\n")

#user input in list
while(line != ""):
    finList.append(tuple(line.split()))
    line = input()
print("Yor List is",finList)

emList(finList)