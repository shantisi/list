num=[50,23,70,56,12,5,10,7]
max=0
max1=0
i=0
while i<len(num):
    if num[i]>max:
        max=num[i]
    if num[i]>max1 and num[i]!=max:
        max1=num[i]
    i=i+1
print(max1)
