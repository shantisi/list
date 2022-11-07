# 31. Given the start and end of a range, write a Python program to print all negative numbers in a given
# range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
# Input: start = -3, end = 4
# Output: -3, -2, -1



a=int(input("enter no"))
while a>0:
    print(-a)
    a=a-1


a=int(input("enter no"))
for a in range(-a,-0):
    print(a)
