n=int(input("enter no"))
b=[]
i=0        
while i<n:
    a=int(input("enter no"))
    b.append(a)
    i=i+1
# print(b)
j=1
while j<=len(b):
    print(b[-j])
    j=j+1

num =int(input("enter no"))
i=0
sum=0
a=[]
while i<num:
    n=int(input("enter no"))
    a.append(n)
    if a[i]%2==0:
        sum =sum+a[i]
    i=i+1
print(a)
print(sum)

a=int(input("enter no"))
if len(str(a))==3:
    b=a%10
    c=a//10
    d=c%10
    e=c//10
    a=(str(b)+str(d)+str(e))
    print(a)
else:
    print("enter the valid 3 diggit num")

i=1
sum=0
while i<=10:
    if i<=5:
        sum=sum+i
        print(sum)
    elif i>=5:
        print(i*i)
    i=i+1

    #   space count

a="my name is priya singh"
i=0
c=0
while i<len(a):
    if a[i]==" ":
        c=c+1
    i=i+1
print(c)

s="my name is priya singh"
i=0
while i<len(s):
    a= s.split(" ")
    i=i+1
print(a)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
i=0
c=[]
while i<len(a):
    c.append(a[i]+b[i])
    i=i+1
print(c)

a=[2,3,4,5,6,7]
b=[3,4,5,6,7,8]
i=0
c=[]
while i<len(a):
    c.append(a[i]*b[i])
    i=i+1
print(c)

a=[2,3,4,5,6,7]
b=[3,4,5,6,7,8]
i=0
c=[]
while i<len(a):
    c.append(a[i]**b[i])
    i=i+1
print(c)


a=[1,2,3,4]
i=0
b=[]
while i<len(a):
    if i==2:
        b.append(10)
    b.append(a[i])
    i=i+1
print(b)


a=[1,3,4,5,6,7]
i=0
sum=0
b=[]
while i<len(a):
    sum=sum+a[i]
    b.append(sum)
    i=i+1
print(b,end=" ")

a=[1,3,4,5,6,7]
i=0
sum=0
b=[]
while i<len(a):
    sum=sum+a[i]
    b.append(sum)
    i=i+1
print([sum],end=" ")



a=[12,0,34,0,5,0,10,0,12]
i=0
b=[]
while i<len(a):
    if a[i]==0:
        pass
    else:
        b.append(a[i])
    i=i+1
i=0
while i<len(a):
    if a[i]!=0:
        pass
    else:
        b.append(a[i])
    i=i+1
print(b)


a=[1,3,4,6,7,8,9]
i=0
c=[]
while i<len(a):
    d=a[i]*2
    c.append(d)
    i=i+1
print(c)

a=[1,3,4,6,7,8,9]
i=0
c=[]
while i<len(a):
    d=a[i]*a[i]
    c.append(d)
    i=i+1
print(c)



a=[2,5,3,4,6,7,8,4,5,9]
i=0
k=3
c=[]
while i<len(a):
    if k==i:
        c.append(10)
        k=k+3
    c.append(a[i])
    i=i+1
print(c) 



# list create

n=int(input("enter no"))
i=0
b=[]
while i<n:
    c=int(input("enter no"))
    b.append(c)
    i=i+1
print(b)

a=[0,1,5,4,0,0,3,0]
i=0
sum=[]
sum2=[]
while i<len(a):
	if a[i] == 0:
		sum=sum+[a[i]]
	else:
		sum2=sum2+[a[i]]
	i=i+1
print(sum2+sum)

a=[1,2,3,0,0,4,0,5,0]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]==0:
        b=b+[a[i]]
    else:
        c=c+[a[i]]
    i=i+1
print(b+c)




a=[102,203,304,405,506]
i=0
b=[]
while i<len(a):
    k=str(a[i])
    s=""
    l=""
    j=0
    while j<len(k):
        if k[j]!="0":
            s=s+k[j]
        else:
            l=l+k[j]
        j=j+1
    b.append(int(s+l))
    i=i+1
print(b)
# output[12,23,34,45,0,0,0,0]


a=[1,2,3,4,5,6,7]
b=[3,4,5,6,7,8,9]
i=0
d=[]
while i<len(a):
    c=a[i]+b[i]
    d.append(c)
    i=i+1
print(d)

a=[10305,12007,304,705,8002]
i=0
f=[]
d=[]
while i<len(a):
    k=str(a[i])
    s=""
    l=""
    j=0
    while j<len(k):
        if k[j]=="0":
            s=s+k[j]
            f.append(int(s))
        else:
            l=l+k[j]
        j=j+1
    d.append(int(s+l))
    i=i+1
print(f+d)

# output [0,0,0,0,12,23,34,45]

a=[1030,1200,705,8002]
i=0
b=[]
while i<len(a):
    k=str(a[i])
    l=" "
    j=0
    while j<len(k):
        if k[j]!="0":
            l=l+k[j]
        j=j+1
    b.append(int(l))
    i=i+1
print(b)


n=[13,12,11,10,9,8,7,6,5,4,3,2,1]
i=0
s=0
c=0
while i<len(n):
    s=s+n[i]
    c=c+1
    i=i+1
print(s//c)
 
# output(midel no)

n=["priya","singh","prachi","more"]
i=0
max=0
b=[]
while i<len(n):
    b=[]
    if len(n[i])>max:
        max=len(n[i])
        c=(n[i])
    i=i+1
    b.append(c)
print(b) 
n=["priya","aradhiysasingh","prachi","more"]
i=0
max=0
while i<len(n):
    b=[]
    if len(n[i])>max:
        max=len(n[i])
        c=(n[i])
    i=i+1
    b.append(c)
print(b) 

a=[6,7,[],8,[1,[],[],2],9]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if a[i][j]!=[]:
                b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)


a=["priya"]
i=0
while i<len(a):
    j=1
    while j<len(a[i])+1:
        print(a[i][-j],end=",")
        j=j+1
    i=i+1
a="priya"
i=0
b=[]
s=5
while i<len(a):
    b.append(a[i])
    b.append(s)
    s=s*2
    i=i+1
print(b)

# nested list creat

n=int(input("enter no"))
i=0
e=[]
while i<n:
    e.append([])
    c=int(input("enter no"))
    j=0
    while j<c:
        e[i].append(j)
        j=j+1
    i=i+1
print(e)

a=int(input("enter no"))
i=0
b=[]
while i<a:
    d=[]
    n=int(input("eneter"))
    d.append(n)
    b.append(d)
    i=i+1
print(b)



    
        
l=[5,6,7,8,5,4,3,2,5,7,8,9,11,15]
i=0
h=[]
j=2
f=6
while i<len(l):
    if i==j:
        h.append(10)
        j=j+6
    if i==f:
        h.append(40)
        f=f+6
    h.append(l[i])
    i=i+1
print(h)

        
l=[5,6,7,8,5,4,3,2,5,7,8,9,11,15]
i=0
h=[]
j=1
f=2
while i<len(l):
    if i==j:
        h.append(10)
        j=j+2
    if i==f:
        h.append(40)
        f=f+2
    h.append(l[i])
    i=i+1
print(h)

a="my name is priya"
i=0
k=" "
while i<len(a):
    s=[]
    if a[i]==str:
        k=" "
        # l.append(a[i])
    else:
        k=k+a[i]
        # l.append(a[i])
    i=i+1
print()


n=[1,2,3,4,5]
i=0
while i<len(n):
    print(n[i],end=" ")
    i=i+1


n=[[1,2,3,4,5],[5,6,7,8,9]]
i=0
while i<len(n):
    if type (n[i])==list:
        j=0
        while j<len(n[i]):
            print(n[i][j],end=" ")
            j=j+1
        i=i+1


i=1
while i<=10:
    print(i)
    (i)-=(-1)

i=2
while i<=10:
    print(i)
    (i)-=(-2)

i=1
while i<=10:
    print(i)
    (i)-=(-2)


n=[1,2,3,4,5,6]
i=0
b=[]
while i<len(n):
    b=b+[n[i]]
    i=i+1
print(b)

a=[10300,1101,7050,80020,00,000]
i=0
b=[]
while i<len(a):
    while a[i]>0:
        if a[i]%10!=0:
            b.append(a[i])
            break
        a[i]//=10
    i=i+1
print(b)

i=-2
while i>=-20:
    print(-i)
    i=i-2
    




