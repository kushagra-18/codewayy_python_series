#Question 4

fileName = input("Please enter the file name:")

#Creating a file, returns error if already present

fileOpen = open("Python_File/"+fileName+".txt", "w")
print("File Created Sucessfully!!")

#Writing to a file

fileWrite = input("Please enter the contents of the file:")

fileOpen.write(fileWrite)

#closing the file
fileOpen.close()