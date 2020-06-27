def stringMiddle(str):
   
#FOR MIDDLE CHAR
    if(len(str) % 2 == 0):
        return "" + str[(int(len(str) / 2) - 1 )] + str[(int(len(str) / 2))]
    else:
        return str[(int(len(str)/2))]
       
#function for vowels
def stringVowel(str):
      numVow = 0
      for i in str:
          if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
              numVow=numVow+1
      print("Number of vowels are:",numVow)
 
# function for string length

def stringWord(str):
    counter = 0    
    for i in str: 
        counter += 1
    print("The length is",counter)
    