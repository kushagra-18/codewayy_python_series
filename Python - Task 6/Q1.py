#Question 1
#Defining functions
def drLec(drSpd):
    if (drSpd <= 70):
        print("OK!!")
    elif (drSpd > 70):
        pen = drSpd - 70
        penPts = pen/5
        print("The Penalty ponits are",penPts)
        if(penPts >= 12):
            print("Licesne Cancelled!!!")
                
drSpd = int(input("Enter Speed:"))  

# Calling the functions
drLec(drSpd)

    