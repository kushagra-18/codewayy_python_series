#Question 6
#Function to check the number
def findType(num):
    sum = 0
    for i in range(1,num):
        if(num % i == 0):
            sum = sum + i
    if(num < sum):
        return -1
        
    elif(num == sum):
        return 0
    else:
        return 1



userNum = int(input("Enter Input:"))

#Calling the function with number as perimeter
findType(userNum)

