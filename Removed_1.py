# 8. The task is to perform the operation of removing all the occurrences of a given item/element present in
# a list.
# Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :
# 2 3 4 5 2
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
# After removing the item, the output list is [2, 3, 4, 5, 2]
# Input :
# 5 6 7 8 9 10
# 7
# Output :
# 5 6 8 9 10 

list=[1,1,2,3,4,5,1,2]
i=0
a=[]
while i<len(list):
    if list[i]!=1:
        a.append(list[i])
    i=i+1
print(a)


list=[5,6,7,8,9,10]
i=0
a=[]
while i<len(list):
    if list[i]!=7:
        a.append (list[i])
    i=i+1
print(a)