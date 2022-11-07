n=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
index=0
while i<len(n):
    b=len(n[i])
    if max<b:
        index=n[i]
    i=i+1
print(max,index)
    


num=[[0],[1,3],[5,7],[9,11],[13,15,17]]
max=0
i=0
while i<len(num):
    if len(num[i])>max:
        max=len(num[i])
        a=num[i]
    i=i+1
print(max,a)

num=[[0],[1,3],[5,7],[9,11],[13,15,17]]
min=len(num[1])
i=0
a=num[1]
while i<len(num):
    if len(num[i])<min:
        min=len(num[i])
        a=num[i]
    i=i+1
print(min,a)





