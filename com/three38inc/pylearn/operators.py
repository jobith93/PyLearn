#!/usr/bin/python3

# created on: 19 July, 2017
# @author: Jobith M Basheer [https://github.com/jobith93]

# Arithmetic Operators
#   Addition        +
#   Subtraction     -
#   Multiplication  *
#   Division        /
#   Modulus         %
#   Exponential     **
#   Floor Division  //


n1 = 20; n2 = 10
print("\nArithmetic Operations")
print(n1, "+", n2, "=", (n1 + n2))
print(n1, "-", n2, "=", (n1 - n2))
print(n1, "*", n2, "=", (n1 * n2))
print(n1, "/", n2, "=", (n1 / n2))
print(n1, "%", n2, "=", (n1 % n2))
print(n1, "**", n2, "=", (n1 ** n2))
print(n1, "//", n2, "=", (n1 // n2))


# Relational Operators
print("\nRelational Operations")
print("50 >= 75 -> ", (50>=75))
print("50 > 75  -> ", (50>75))
print("50 == 75 -> ", (50==75))
print("50 <= 75 -> ", (50<=75))
print("50 < 75  -> ", (50<75))


# Logical Operators
#   or
#   and
#   negate

print("\nRelational Operations")
isPlay = True
isKid = True
if isKid and isPlay:
    print("Kid is happy")


# Assignment Operators
#   =
#   +=
#   -=
#   *=
#   /=


# Membership Operators
print("\nMembership Operations")
names = ["sonu", "joel", "jobith"]
print(names)
print("Type of names: ", type(names), "\n")

print("`sonu` is part of the list: ", "sonu"in(names))
print("`jijo` is part of the list: ", "jijo"in(names))
print("`joel` is part of the list: ", "joel"in(names))

# Identity Operators