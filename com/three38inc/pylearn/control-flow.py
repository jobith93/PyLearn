#!/usr/bin/python3

# created on: 19 July, 2017
# @author: Jobith M Basheer [https://github.com/jobith93]

# Control Flow Statements
#
#   Decision Making
#       if
#       if-else
#       elif
#
#   Looping
#       for
#       while
#       do while
#       foreach
#
#   Control Statements
#       break
#       continue
#       pass

print("\nControl Flow Statements")
discount = 25
if discount > 20:
    print("Special Discount:", discount)


marks = 70
if 100 > marks > 80:
    print("Grade: Distinction")
elif 80 > marks > 60:
    print("Grade: First Class")
elif 60 > marks > 40:
    print("Grade: Second Class")
elif 40 > marks > 0:
    print("Grade: Fail")
else:
    print("Invalid Marks")


print("\nNumbers:", end=" ")
for num in range(1, 6):
    print(num, end=", ")


marks = [44, 78, 55, 21, 98]
print("\nMarks:", end=" ")
for mark in marks:
    print(mark, end=", ")


# continue
print("\nNumbers:", end=" ")
for num in range(1, 10):
    print(num, end=", ")
    if num == 5:
        continue


# break
print("\nNumbers:", end=" ")
for num in range(1, 10):
    print(num, end=", ")
    if num == 5:
        break


# pass
print("\nNumbers:", end=" ")
for num in range(1, 10):
    print(num, end=", ")
    if num == 5:
        pass    # NOP

