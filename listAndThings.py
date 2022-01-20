#Aarian Dhanani
#1/20/22
#List, tuple, dictionary, set

import os
os.system('clear')

fruits = ["orange", "apple", 1, 1.05, "banana"]
print(len(fruits))
for elem in fruits:
    print(type(elem))

myList = list((3,5,6))
print(myList)

fruits.append("kiwi")
fruits.insert(3, 'grapes')

fruits.append(myList)
print(fruits)