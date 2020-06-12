#Dictionary
#Diesese name is written in 'key' and year of epidemic is in 'values'

pan_dict = {"COVID-19":2019, "Spanish FLu":1918, "Ebola":2014,"H1N1":2009}
print(pan_dict)

#The keys() function will retirn the key of a dict, i.e disease name
print(pan_dict.keys())

#The items() fucntion will return the dictionary with both keys and values which is called an item
print(pan_dict.items())

#The values() function will return the list of values i.e year
print(pan_dict.values())

#Changing the year of Spanish flu, key to 1919
pan_dict["Spanish Flu"]= 1919
print(pan_dict)

#Looping through dictionary, printing all key name one by on
for x in pan_dict:
  print(x)

#Looping through dictionary, printing all the values one by on
for x in pan_dict.values():
  print(x)

#Looping through dictionary, printing all the keys and values one by on
for x, y in pan_dict.items():
  print(x, y)

#Adding new items
pan_dict["Plague"] = "1620"
print(pan_dict)