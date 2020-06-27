import list

userChoice = input(("Please Enter the choice:[A- for list, B- String, C-Operator]"))

if(userChoice == 'A'):
    minList = list.minmaxList()
    list.smallNum(minList)
    list.maxNum(minList)
    list.sumFunc(minList)

    elif (userChoice == "B"):
	str = input("Enter the Word:")

	string.stringWord(str)
	string.stringVowel(str)
	string.stringMiddle(str)
        

    elif (userChoice == "C"):
        #entering input
        testA = int(input("Enter the number:"))
        testB = int(input("Enter the number:"))
        testC = int(input("Enter the number:"))
        
        #calling function
        operator.logAnd(testA,testB,testC)
        operator.logOR(testA,testB,testC)
        operator.logNot(testA)
        
    
