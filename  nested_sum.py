list=[3005,40600,2340700,305]
i=0
d=[]
while i<len(list):
    if list[i]%10!=0:
        d.append(list[i])
    else:
        r=list[i]//100
        d.append(r)
    i=i+1
print(d)


n=[1,2,[4,3,2],[4,8],8]
i=0
sum=0
while i<len(n):
    if type(n[i])==list:
        j=0
        while j<len(n[i]):
            sum=sum+n[i][j]
            j=j+1
    else:
        sum=sum+n[i]
    i=i+1
print(sum)


n=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
sum=0
while i<len(n):
    if type (n[i])== list:
        j=0
        while j<len(n[i]):
            sum=sum+n[i][j]
            j=j+1
    else:
        sum=sum+n[i]
    i=i+1
print(sum)