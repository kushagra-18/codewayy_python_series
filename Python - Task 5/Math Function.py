#Question 2
#Using Math functions
import math as m

Num = int(input('Enter the Number:'))

#sqrt function
print("Square root of the number will be:",m.sqrt(Num))

#fcatorial
print("The factorial of the number will be:",m.factorial(Num))

#pow
numPow = int(input("Enter the power:"))
print("Number raised to the given power is:",m.pow(Num,numPow))

#Using Sorting

#Function for List
def sortList():
    myList = []
    n = int(input("Enter the length of list:"))
    for num in range(n):
        listElement = int(input("Enter elements:"))
        myList.append(listElement)
    print("Your List is:",myList)
    
