list=[6,1,3,5,6,3,1]
i=0
a=[]
pro=1
while i<len(list):
    if list[i] not in a:
        a.append(list[i]) 
        pro=pro*list[i]
    i=i+1
print(a)
print(pro)
