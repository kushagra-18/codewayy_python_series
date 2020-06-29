#Using Sorting

#Function for List
def sortList():
    myList = []
    n = int(input("Enter the length of list:"))
    for num in range(n):
        listElement = int(input("Enter elements:"))
        myList.append(listElement)
    print("Your List in is:",myList)
    #Sorting the List
    
    myList.sort()
    print("Your list sorted in accesnding order:",myList)

#Fucntion of tuple
def sorTup():
    tupList = []
    line = input("Enter the list of tuples:\n")
    while(line != ""):
        tupList.append(tuple(line.split()))
        line = input()
    print("The Tuple is:",tupList)
    sortedTup = sorted(tupList)
    print("The sorted tuple is:",sortedTup)

#Function for set
def sortSet():
     mySet = set()
     n = int(input("Enter the length of list:"))
     for num in range(n):
        setElement = int(input("Enter elements:"))
        mySet.add(setElement)
     
    #Sorting in a set
     sortedSet = sorted(mySet)
     print("Your sorted set is:",sortedSet)

#Python dictionary
def sortDict():
    myDict = {}
    
    #Adding elements in dictionary
    num = int(input("How many values you want to input:"))
    for i in range (num):
        dictObj = input("Enter Value:")
        dictKey = int(input("Enter keys:"))
        myDict[dictObj] = dictKey
    print("The dictionary is:",myDict)
    
    #Sorting
    sortOrders = sorted(myDict.items(), key=lambda x: x[1], reverse=True)
    print("Sorted by Object:",sortOrders)
 
     
userCh = input("Enter The choice [A -> List, B -> Tuple , C -> Sets, D -> Dict]")
if(userCh == "A"):
    sortList()
elif(userCh =="B"):
    sorTup()
elif(userCh =="C"):
    sortSet()
elif(userCh =="D"):
    sortDict()
        