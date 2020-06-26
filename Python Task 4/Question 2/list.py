# function for max and min in as list
def minmaxList():
    myList = []
# entering the numbers in the list
    n = int(input("ENter the length of string:"))
    for num in range(n):
        listElement = int(input("Enter elements:"))
        myList.append(listElement)
    #print("Your List is:",myList)
    return myList;

minList = minmaxList()
#print(minList[])


#for minimum
smallNum = minList[0] 
for j in minList:
    if(smallNum > j):
        smallNum = j
print("The minimum element is:"smallNum)

#for maximum
maxNum = minList[0] 
for j in minList:
    if(maxNum < j):
        maxNum = j
print("The maximum element is:"maxNum)