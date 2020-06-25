#Question 3
#Using for loop

print("For loop:")
for i in range(1,11):
    if(i!=3 and i!=7):
        print(i)
       
#Using while loop

print("while loop:")
i=1
while(i<=10):
    if(i==3 or i==7):
        i=i+1
    else:
        print(i)
        i=i+1