#Question3
def strCase(userStr):
    upCase =0
    lowCase =0 
    for i in userStr:
        ascNum = ord(i)
        #print(ascNum)
        if((ascNum >= 65 and ascNum <=90)):
            upCase = upCase + 1
        else:
           lowCase = lowCase + 1
    print("Uppercase Letters:",upCase)
    print("Lowercase letters:",lowCase)

           #Input a string from user
userStr = input('Enter a string:')
strCase(userStr)
    