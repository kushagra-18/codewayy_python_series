#Question 6
#Function to check the number
def findType(n):
    i = 1
    j = 1
    sum = 0
    for i in range(n):
        for j in range(n):
            if (i * j == n):
                sum = sum + i
                sum = sum + j
            if sum > n:
                return -1
            elif sum < n:
                return 1
            else:
                break
    return 0



userNum = int(input("Enter Input:"))

#Calling the function with number as perimeter
findType(userNum)

