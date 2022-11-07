elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
evensum=0
oddsum=0
c=0
c1=0
while i<len(elements):
    if elements[i]%2==0:
        c=c+1
        evensum=evensum+elements[i]
        avg=evensum/c
    elif elements[i]%2!=0:
        c1=c1+1
        oddsum=oddsum+elements[i]
        avg1=oddsum/c1
    i=i+1
print(avg,"even",c)
print(avg1,"odd",c1)

a=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
print(b)
print(c)