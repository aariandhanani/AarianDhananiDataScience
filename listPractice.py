#Aarian Dhanani
#1/23/22
#List practice homework assignment

import os
os.system('clear')


#Problem 1
list1 = [15, 100, 154, 20, 253, 530, 203]
value = 0
for i in list1:
    if (i == 20):
        list1[value] = 200
    value = value + 1

print(list1)


#Problem 2
#I can't tell if I'm supposed to remove the value 20 or replace it with 200 because the instructions do not match the example given. I will replace it with 200 because the next question asks me to remove occurances of 20 as well.
list1 = [5, 20, 15, 20, 25, 50, 20]
value = 0
for i in list1:
    if (i == 20):
        list1[value] = 200
    value = value + 1

print(list1)


#Problem 3
list1 = [5, 20, 15, 20, 25, 50, 20]
value = 0
for i in list1:
    if (i == 20):
        list1.remove(20)
    value = value + 1

print(list1)


#Problem 4
#I don't need to use the filter() function for this.
list1 = list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
value = 0
for i in list1:
    if (i == ""):
        list1.remove("")
    value = value + 1

print(list1)


#Problem 5
#Really liked this problem. Pretty interesting stuff.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


#Problem 6
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#list1[2][1].append(["h", "i", "j"])
list1[2][1][2].extend(["h", "i", "j"])
print(list1)


#Problem 7
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
value = 0
while(value != len(list1)):
    print(list1[value], list2[3-value])
    value = value + 1


#Problem 8
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
value = 0
while(value != len(list1)):
    list3.append(list1[value] + list2[value])
    value = value + 1
print(list3)


#Problem 9
numbers = [1, 2, 3, 4, 5, 6, 7]
value = 0
while(value != len(numbers)):
    numbers[value] = numbers[value] * numbers[value]
    value = value + 1
print(numbers)


#Problem 10
phrase = " The best class in Greenhill is Data Science"
phraseList = []
currentWord = ""
value = 1
while(value != len(phrase)):
    if(phrase[value] == " "):
        phraseList.append(currentWord)
        currentWord = ""
    else:
        currentWord = currentWord + phrase[value]
    value = value + 1
print(phraseList)