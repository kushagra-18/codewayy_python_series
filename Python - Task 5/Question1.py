#Exception handling -- Q1
#Taking input
try:
    phNum = input("Please Enter a valid Mobile Number:")
    strLen = len(phNum)
    if( strLen!= 10 ):
        raise Exception
 
#Error message if number is invalid

except Exception:
    print("Error!!!! Your number is invalid!!")

else:
    print("Your Mobile Number is:",phNum)
    
    