# 24. Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

list=[1,2,3,1,2,3]
i=0
a=[]
while i<len(list):
    if list [i] not in a:
        a.append (list[i])
    i=i+1
print(a)
    
