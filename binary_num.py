a=[1,0,1,0]
b=0
i=-1
sum=0
while i>=-len(a):
    sum=sum+a[i]*2**b
    b=b+1
    i=i-1
print(sum)
