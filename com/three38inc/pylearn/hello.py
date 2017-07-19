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


# strings
name = "Jobith M Basheer"
print(name, "Bangalore")
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("M Basheer", "MB"))
print(("  "+name+"  ").strip())
print(name.split(" "))
print(name[2:6])
print(name[:6])
print(name[7:])
