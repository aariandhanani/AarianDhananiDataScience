#Aarian Dhanani
#January 13th, 2022
#String and List

import os, sys, random
os.system("clear")

# num1 = 8
# num2 = 4.5
# char = "t"
# flag = False

# stringVar1 = "Hello there"
# stringVar2 = " goodbye there"

# print(stringVar1 + " " + stringVar2)
# print(stringVar1 + " " + str(num1) + stringVar2)

# print(type(num2))
# print(stringVar1[1])
# #del stringVar1[4]
# #print(stringVar1)

# print("Hello \t Peter \n I am here\\or not \"Goodbye\"")

# for letter in stringVar1:
#     print(letter, end = ' ')
# print()
# for i in range(8):
#     print(i, end = ' ')
# print()
# for i in range(10,21):
#     print(i, end = ' ')
# print()

# if(marioSize > 25 or marioSize < 1):
#         print("Size accepted.")
# else:
#     print("Please enter a size between 1 and 25")
# try:
#     marioSize = input("What size would you like? ")
#     sizeValue = int(marioSize)
#     if(marioSize > 25 or marioSize < 1):
#         print("Size accepted.")
# except ValueError:
#     print("Please enter a number between 1 and 25")

play = 1

while (play == 1):
    marioSize = input("What size would you like? ")
    sizeValue = int(marioSize)
    if(sizeValue < 26 and sizeValue > 0):
        print("Size accepted.")
        for i in range(0,sizeValue):
            for j in range(0,(sizeValue-i)):
                print("", end = " ")
            for j in range(0,(i+1)):
                print("x", end = "")
            print("  ", end = "")
            for j in range(0,(i+1)):
                print("x", end = "")
            print()
    elif (sizeValue == -1):
        break
    else:
        print("Invalid size. Please enter a size between 1 and 25.")
    sizeValue = 0

print("Thanks for playing.")