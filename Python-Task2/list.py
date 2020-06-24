#Initialisng a list
panList = ["COVID-19", "Spanish FLu", "Ebola", "H1N1","SARS","MERS"]
print(panList)

#Acessing items
print(panList[2])

#Change Item Value
panList[5] = "Middle-Eastern respirartory syndrome"
print(panList)

#looping though list
for x in panList:
    print(x)
    
#Adding items using append
panList.append("Polio")
print(panList)

#adding item at specific postion using insert function
panList.insert(2,"AIDS")
print(panList)

#deleting an item using remove
panList.remove("SARS")
print(panList)

#removing using pop, The pop() method removes the specified index, (or the last item if index is not specified)
panList.pop()
print(panList)

#joing two lists
count_list = [1,2,3,4,5,6]
print(count_list+panList)

#use extend() method to add list2 at the end of list1:
panList.extend(count_list)
print(panList)