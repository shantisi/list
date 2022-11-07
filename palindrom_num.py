a=["prachi","priya","more","jeet"]
i=0
b=[]
while i<len(a):
    c=(a[i][::-1])
    b.append(c)
    i=i+1
print(b)

# output["ihcarp","ayirp","erom","teet"]


n=["noun","mom","sis","132","1221"]
i=0
b=[]
c=0
while i<len(n):
    d=(n[i][::-1])
    if n[i]==d:
        b.append(d)
        c=c+1
    i=i+1
print(b,c)


# output["mom","sis","1221"]

