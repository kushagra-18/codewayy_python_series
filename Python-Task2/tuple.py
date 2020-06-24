#Tuple
panTup = ("COVID-19", "Spanish FLu", "Ebola", "H1N1","SARS","MERS")
print(panTup)

#accesing tuple items
print(panTup[2])

#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item,
print(panTup[-1])

#Range of Indexes
print(panTup[2:4])

#Looping through a tuple
for x in panTup:
    print(x)
    
#Tuple Length, To determine how many items a tuple has
print(len(panTup))

#Adding two tuples
pan_count_tup=(1,2,3,4,5,6)
totTup = pan_Count_tup+panTup
print(totTup)

#Using the tuple() method to make a tuple
newTup = tuple(("COVID-19", "Spanish FLu", "Ebola", "H1N1","SARS","MERS"))
print(newTup)
