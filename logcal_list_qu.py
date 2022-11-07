a=[1,2,3,4,5,6,7,8,9]
a.append(1)
print(a)

a=[1,2,3,4,5,6,7,8,9]
b=["a","b","c","d","e","f"]
a.extend(b)
print(a)

a=[1,2,3,4,5,6,7]
a.extend([11,12])
print(a)



a=[1,2,3,4,5,6,7,8,9,10]
a.insert(9,"apple")
print(a)


a=[1,2,3,4]
a.pop()
a.append(5)
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
a.pop(9)
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
del a[0]
print(a)

a=[1,2,3,4,5,6,7,8,9,10]
a.clear()
print(a)



list=[1,2,5,4,6,5,8,7,9,10]
list.sort()
print(list)

list=[1,2,5,4,6,5,8,7,9,10]
list.sort(reverse=True)
print(list)

list=[1,2,5,4,6,5,8,7,9,10]
length=len(list)
print(length)

list=[1,2,3,4,59,8,70]
max=max(list)
print(max)

list=[3,4,5,6,7,8,1]
min=min(list)
print(min)

#      index
n=[1,2,3,4,5,6,7,8,9]
a=n[4]
print(a)
   
#    slicing
list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[0:3]
print(list1)


list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[0:5:2]
print(list1)

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[5:]
print(list1)

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[:5]
print(list1)


        #  reverse slicing

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[::-1]
print(list1)

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[:1:-1]
print(list1)

#            remove

a=[1,2,3,4,5,6,7]
a.remove(2)
print(a)

#         sum

a=[1,2,3,4,5,6,7,8]
sum=sum(a)
print(sum)

a=[2,3,4,5,6,7,8]
a.reverse()
print(a)
      
#       count
list=[1,2,3,2,2,2,4,5,6]
a=list.count(2)
print(a)

a=[23,56,20,12]
l1=sorted(a)
print(l1)

a=[2,5,4,6,8,7,11,8]
b=sorted(a,reverse=True)
print(b)


# list creating

a=[]
n=int(input("enter no"))
i=0
while i<(n):
    val=int(input("enter no"))
    a.append(val)
    i=i+1
print(a)

# list create sum

a=[]
n=int(input("enter no"))
i=0
sum=0
while i<(n):
    val=int(input("enter no"))
    sum=sum+val
    a.append(val)
    i=i+1
print(a)
print(sum)


a=int(input("enter no"))
i=0
s=[]
while i<a:
        s.append([])
        n=int(input("enter the no:"))
        j=0
        while j<n:
                s[i].append(j)
                j=j+1
        i=i+1
print(s)

a=[1,3,4,5,[6,7],8,9,[10,11,[12],16],1]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum=sum+a[i][j][k]
                    k=k+1
            else:
                sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)

a=[1,3,[4,5],2,[10,11,16],1,12]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)

n=int(input("enter no"))
i=0
c=0
b=[]
print(a)



list=[1,2,5,4,6,5,8,7,9,10]
list.sort()
print(list)

list=[1,2,5,4,6,5,8,7,9,10]
list.sort(reverse=True)
print(list)

list=[1,2,5,4,6,5,8,7,9,10]
length=len(list)
print(length)

list=[1,2,3,4,59,8,70]
max=max(list)
print(max)

list=[3,4,5,6,7,8,1]
min=min(list)
print(min)

    #  index
n=[1,2,3,4,5,6,7,8,9]
a=n[4]
print(a)
   
#    slicing
list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[0:3]
print(list1)


list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[0:5:2]
print(list1)

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[5:]
print(list1)

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[:5]
print(list1)


        #  reverse slicing

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[::-1]
print(list1)

list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
list1=list[:1:-1]
print(list1)

        #    remove

a=[1,2,3,4,5,6,7]
a.remove(2)
print(a)

        # sum

a=[1,2,3,4,5,6,7,8]
sum=sum(a)
print(sum)

a=[2,3,4,5,6,7,8]
a.reverse()
print(a)
      
#       count
list=[1,2,3,2,2,2,4,5,6]
a=list.count(2)
print(a)

a=[23,56,20,12]
l1=sorted(a)
print(l1)

a=[2,5,4,6,8,7,11,8]
b=sorted(a,reverse=True)
print(b)


# list creating

a=[]
n=int(input("enter no"))
i=0
while i<(n):
    val=int(input("enter no"))
    a.append(val)
    i=i+1
print(a)

# list create sum

a=[]
n=int(input("enter no"))
i=0
sum=0
while i<(n):
    val=int(input("enter no"))
    sum=sum+val
    a.append(val)
    i=i+1
print(a)
print(sum)


a=int(input("enter no"))
i=0
s=[]
while i<a:
        s.append([])
        n=int(input("enter the no:"))
        j=0
        while j<n:
                s[i].append(j)
                j=j+1
        i=i+1
print(s)

a=[1,3,4,5,[6,7],8,9,[10,11,[12],16],1]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum=sum+a[i][j][k]
                    k=k+1
            else:
                sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)



n=int(input('enter the no'))
count=0
i=1
b=[]
while i<=n:
    if n%i==0:
        ount=count+1
    i=i+1
    b.append(n)
if count==2:
    print(b,"prime")
else:
    print(b,"not prime")












