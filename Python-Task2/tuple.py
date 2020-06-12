#Tuple
pan_tup = ("COVID-19", "Spanish FLu", "Ebola", "H1N1","SARS","MERS")
print(pan_tup)

#accesing tuple items
print(pan_tup[2])

#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item,
print(pan_tup[-1])

#Range of Indexes
print(pan_tup[2:4])

#Looping through a tuple
for x in pan_tup:
    print(x)
    
#Tuple Length, To determine how many items a tuple has
print(len(pan_tup))

#Adding two tuples
pan_count_tup=(1,2,3,4,5,6)
tot_tup=pan_count_tup+pan_tup
print(tot_tup)

#Using the tuple() method to make a tuple
new_tup=tuple(("COVID-19", "Spanish FLu", "Ebola", "H1N1","SARS","MERS"))
print(new_tup)
