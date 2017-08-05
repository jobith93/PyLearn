#!/usr/bin/python3

# created on: 19 July, 2017
# @author: Jobith M Basheer [https://github.com/jobith93]

# Built In Types
# 1. Sequence Types
#   -> list
#   -> tuple
#   -> strings

# creating a list
cities = ["New York", "Chicago", "London",  "Bengaluru"]
print("Create:", cities)
print("Type of `cities`:", type(cities))

# Operations on List
# Append
cities.append("Kochi")
print("Append:", cities)


# Read
print("Read:  ", cities[1:3])
print("Read:  ", cities[:3])
print("Read:  ", cities[2:])


# Update
cities[2] = "Brimingham"
print("Update:", cities)

# Delete
cities.remove("Kochi")
# cities.clear()
print("Remove:", cities)

cities.pop()
print("Pop:   ", cities)


# Sorting
cities.sort()
print("Sort:  ", cities)


