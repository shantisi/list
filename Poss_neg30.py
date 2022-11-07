# 30. Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

list=[2, -7, 5, -64, -14]
i=0
poss=0
neget=0
while i<len(list):
    if list[i]>0:
        poss=poss+1
    else:
        neget=neget+1
    i=i+1
print(poss,"poss number")
print(neget,"neget")


list=[-12, 14, 95, 3]
i=0
poss=0
negat=0
c=0
while i<len(list):
    if list[i]>0:
        poss=poss+1
    else:
        negat=negat+1
    i=i+1
print(poss,"poss")
print(negat,"negat")



