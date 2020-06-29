#Question 3
#using exception handling
try:
    with open("Python_File/tasks.md","r") as f:
        f_contents = f.read()

        
except Exception:
    print("Error 404...File not found !!")
else:
    print(f_contents)
    