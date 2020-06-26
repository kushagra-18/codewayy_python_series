
#And operator
def logAnd(a,b,c):
    if a > 0 and b > 0: 
        print("The numbers are greater than 0") 
  
    if a > 0 and b > 0 and c > 0: 
        print("The numbers are greater than 0") 
    else: 
        print("Atleast one number is not greater than 0")

#or operator       
def logOR(a,b,c):
    if a > 0 or b > 0: 
        print("Either of the number is greater than 0") 
    else: 
        print("No number is greater than 0") 
  
    if b > 0 or c > 0: 
        print("Either of the number is greater than 0") 
    else: 
        print("No number is greater than 0") 
#not operator        
def logNot(x):
    print(not(x > 3 and x < 10))
        
    
        
        
        
        
        
        
        
        
   