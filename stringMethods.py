#Aarian Dhanani
#January 18th, 2022
#String Methods

import os

#casefold
string1 = "I AM DOING WELL"
print(string1)
string1CaseFold = string1.casefold()
print(string1CaseFold)
print()

#count
string1 = "I AM DOING WELL. HOW ARE YOU DOING?"
print(string1)
string1 = string1.count("DOING")
print(string1)
print()

#endswith
string1 = "I AM DOING WELL. HOW ARE YOU DOING?"
print(string1)
string1 = string1.endswith("?")
print(string1)
print()

#find
string1 = "I AM DOING WELL. HOW ARE YOU DOING?"
print(string1)
string1 = string1.find(".")
print(string1)
print()

#format_map
format1 = {"hi":1, "bye":0}
print("{hi} {bye}".format_map(format1))
print()

#isalnum
string1 = "I AM DOING WELL. HOW ARE YOU DOING?"
print(string1)
string1 = string1.isalnum()
print(string1)
print()

#isdecimal
string1 = "I AM DOING WELL. HOW ARE YOU DOING?"
print(string1)
string1 = string1.isdecimal()
print(string1)
print()

#isidentifier
string1 = "iamdoingwell"
print(string1)
string1 = string1.isidentifier()
print(string1)
print()

#isnumeric
string1 = "1245678910"
print(string1)
string1 = string1.isnumeric()
print(string1)
print()

#isspace
string1 = "     "
print(string1)
string1 = string1.isspace()
print(string1)
print()

#isupper
string1 = "HELLO"
print(string1)
string1 = string1.isupper()
print(string1)
print()

#ljust
string1 = "I am doing well."
print(string1)
string1 = string1.ljust(50)
print(string1, "How are you doing?")
print()

#lstrip
string1 = "I am doing well."
print(string1)
string1 = string1.lstrip()
print("How are you doing? ", string1, " How are you doing?")
print()

#partition
string1 = "I am doing well."
print(string1)
string1 = string1.partition("doing")
print(string1)
print()

#rfind
string1 = "Hello how are you? I'm good, how are you?"
print(string1)
string1 = string1.rfind("you")
print(string1)
print()

#rjust
string1 = "Hello how are you? I'm good, how are you?"
print(string1)
string1 = string1.rjust(15)
print(string1, "I'm good, thanks!")
print()

#rsplit
string1 = "Hello how are you?  I'm good, how are you?"
print(string1)
string1 = string1.rsplit("  ")
print(string1)
print()

#split
string1 = "Hello how are you?  I'm good, how are you?"
print(string1)
string1 = string1.split("  ")
print(string1)
print()

#startswith
string1 = "Hello how are you?  I'm good, how are you?"
print(string1)
string1 = string1.startswith("Hello")
print(string1)
print()

#swapcase
string1 = "Hello how are you?  I'm good, how are you?"
print(string1)
string1 = string1.swapcase()
print(string1)
print()

#translate
string1 = "Hi! Ok bye..."
print(string1)
format2 = {105:97}
print(string1.translate(format2))
print()

#zfill
string1 = "Hello how are you?  I'm good, how are you?"
print(string1)
string1 = string1.zfill(100)
print(string1)
print()