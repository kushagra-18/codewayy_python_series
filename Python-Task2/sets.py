s#Sets
#intialising sets
panSet = {"COVID-19", "Spanish FLu", "Ebola"}
print(panSet)

#Accesing sets through loops
for x in panSet:
    print(x)
    
#Adding item using add fucntion
panSet.add("Polio")
print(panSet)

#Adding multiple items using update fucntion
panSet.update(["Polio","AIDS"])
print(panSet)

#getting the length
print(len(panSet))

#Removing items using discard fucntion
panSet.discard("AIDS")
print(panSet)

#deleting using pop
x=panSet.pop()
print(x)
print(panSet)

#Using the union function to return the union of two sets
panSet2 = {"COVID-19", "Spanish FLu", "Ebola"}
main_set = union(panSet2)
print(main_set)