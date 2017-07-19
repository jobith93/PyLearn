#!/usr/bin/python3

# While Loop
# Simple Fibonacci Series
# Sum of two elements defines the next

a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
print("End.")


# For Loop
# read lines from the file

fh = open("assets/lines.txt")
for line in fh.readlines():
    print(line, end='')

