#Initialisng a list
pan_list = ["COVID-19", "Spanish FLu", "Ebola", "H1N1","SARS","MERS"]
print(pan_list)

#Acessing items
print(pan_list[2])

#Change Item Value
pan_list[5] = "Middle-Eastern respirartory syndrome"
print(pan_list)

#looping though list
for x in pan_list:
    print(x)
    
#Adding items using append
pan_list.append("Polio")
print(pan_list)

#adding item at specific postion using insert function
pan_list.insert(2,"AIDS")
print(pan_list)

#deleting an item using remove
pan_list.remove("SARS")
print(pan_list)

#removing using pop, The pop() method removes the specified index, (or the last item if index is not specified)
pan_list.pop()
print(pan_list)

#joing two lists
count_list=[1,2,3,4,5,6]
print(count_list+pan_list)

#use extend() method to add list2 at the end of list1:
pan_list.extend(count_list)
print(pan_list)