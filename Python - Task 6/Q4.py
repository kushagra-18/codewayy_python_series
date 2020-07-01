#Question 4

def atOcc(userStr1):
    for i in userStr1:
        userStr1 = userStr1.lower()
    print("number of occurences:",(userStr1.count("at")))
        

userStr1 = input("String:")
atOcc(userStr1)
        