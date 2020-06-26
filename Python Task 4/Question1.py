# initializing N 
N = int(input("Enter the value of N:"))


# matrix creation of n * n 
matPrime = [list(range(1 + N * i, 1 + N * (i + 1))) 
                            for i in range(N)] 

# print result 
print("The matrix is:" + str(matPrime)) 


# New list is defined
newMat = [] 

# Nested lists are transformed into single list

for i in matPrime: 
    for j in i: 
        newMat.append(j)
print(newMat)

# Searching for prime numbers
for num in newMat:
    if num > 1:
        for j in range(2,num):
            if(num%j == 0):
                break
        else:
            print(num)