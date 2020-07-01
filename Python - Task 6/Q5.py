#Question 5

def cntWord(userWord):
    numWord = 0
    for i in userWord:
        if(i == " "):
            numWord = numWord + 1
    print("number of words are:",numWord+1)

#User input

userWord = input("Enter a string:")
cntWord(userWord)
    