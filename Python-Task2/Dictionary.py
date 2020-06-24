#Dictionary
#Diesese name is written in 'key' and year of epidemic is in 'values'

panDict = {"COVID-19":2019, "Spanish FLu":1918, "Ebola":2014,"H1N1":2009}
print(panDict)

#The keys() function will retirn the key of a dict, i.e disease name
print(panDict.keys())

#The items() fucntion will return the dictionary with both keys and values which is called an item
print(panDict.items())

#The values() function will return the list of values i.e year
print(panDict.values())

#Changing the year of Spanish flu, key to 1919
panDict["Spanish Flu"]= 1919
print(panDict)

#Looping through dictionary, printing all key name one by on
for x in panDict:
  print(x)

#Looping through dictionary, printing all the values one by on
for x in panDict.values():
  print(x)

#Looping through dictionary, printing all the keys and values one by on
for x, y in panDict.items():
  print(x, y)

#Adding new items
panDict["Plague"] = "1620"
print(panDict)