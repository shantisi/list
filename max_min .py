num=[[0],[1,3],[5,7],[9,11],[13,15,17]]
min=len(num[1])
max=0
i=0
a=num[1]
while i<len(num):
    if  len(num[i])>max:
        max =len(num[i])
        b=(num[i])
    if len(num[i])<min:
        min=len(num[i])
        a=num[i]
    i=i+1
print(max,b)
print(min,a)

