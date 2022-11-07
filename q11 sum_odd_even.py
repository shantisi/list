s=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
evensum=0
oddsum=0
c=0
c1=0
while i<len(s):
    if s[i]%2==0:
        c=c+1
        evensum=evensum+s[i]
    elif s[i]%2!=0:
        c1=c1+1
        oddsum=oddsum+s[i]
    i=i+1
print(evensum,)
print("count","evensum",c)
print(oddsum,)
print("count","oddsum",c1)

s=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
a=[]
b=[]
while i<len(s):
    if s[i]%2==0:
        sum=sum+s[i]
        a.append(s[i])
    else:
        sum1=sum1+s[i]
        b.append(s[i])
    i=i+1
print(a,sum)
print(b,sum1)

s=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[]
b=[]
while i<len(s):
    if s[i]%2==0:
        a.append(s[i])
    else:
        b.append(s[i])
    i=i+1
print(a,"even")
print(b,"odd")



