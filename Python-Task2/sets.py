#Sets
#intialising sets
pan_set={"COVID-19", "Spanish FLu", "Ebola"}
print(pan_set)

#Accesing sets through loops
for x in pan_set:
    print(x)
    
#Adding item using add fucntion
pan_set.add("Polio")
print(pan_set)

#Adding multiple items using update fucntion
pan_set.update(["Polio","AIDS"])
print(pan_set)

#getting the length
print(len(pan_set))

#Removing items using discard fucntion
pan_set.discard("AIDS")
print(pan_set)

#deleting using pop
x=pan_set.pop()
print(x)
print(pan_set)

#Using the union function to return the union of two sets
pan_set2={"COVID-19", "Spanish FLu", "Ebola"}
main_set=union(pan_set2)
print(main_set)