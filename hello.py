#!/usr/bin/python3
import keyword

print("Hello, World!")

# variables
x = 10
#x = input("Enter a number: ")

print(x)

# keyword list
print(keyword.kwlist)

if keyword.iskeyword("name"):
    print("`name is a keyword!`")
else:
    print("`name is not a keyword!`")