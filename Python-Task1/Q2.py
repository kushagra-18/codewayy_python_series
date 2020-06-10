#Question 2
#Information
fname=input("Enter First Name:")
lname=input("Enter Last Name:")
cname=input("Enter your college name:")
cadd=input("Enter your college address:")
#Marks
mark1=float(input("Enter marks of Subject 1:"))
mark2=float(input("Enter marks of Subject 2:"))
mark3=float(input("Enter marks of Subject 3:"))
mark4=float(input("Enter marks of Subject 4:"))
mark5=float(input("Enter marks of Subject 5:"))
#Calculation
tot=mark1+mark2+mark3+mark4+mark5
per=(tot/5)
#Output
print("Your name",fname + lname)
print("College name and adress:",cname + cadd)
print("Total Marks:",tot,"Percentage",per,"%")