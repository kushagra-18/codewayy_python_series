def check_marks():
    stMrk = int(input("Please Enter the marks:"))
    
    #Using try and catch blocl
    try:
        if(stMrk <90):
            raise Exception
                
    except Exception:
        print("Not Eligible!!!")
        
    else:
        return 0
    
#calling the functions    
check_marks()