n=[[0],[1,3],[5,7],[9,11],[13,15,17]]
min=len(n[1])
i=0
a=len(n[i])
while i<len(n):
    if len(n[i])< min:
        min=len(n[i])
        a=n[i]
    i=i+1
print(min,a)

a=[1,2,3,4,5,6,7,8]
i=0
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print([min]) 