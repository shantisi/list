a=int(input("enter prime num"))
count=0
i=1
while i<=a:
    if a%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime")
else:
    print("not")


a=int(input("enter prime num"))
i=1
count=1
while a[i]<len(a):
    if a%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime")
else:
    print("not prime")
    