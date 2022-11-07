# 26. Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22

list=[4,5,5,5,3,8]
i=1
a=[]
while i<len(list):
    if list[i] not in a:
        a=list[i]
    i=i+5
print(a)


list=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=2
a=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i=i+4
print(a)






