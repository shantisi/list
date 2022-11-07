n=[1,1,2,3,4,4,5,1]
i=0
a=[]
while i<len(n):
    j=0
    c=0
    while j<len(n):
        if n[i]==n[j]:
            c=c+1
        j=j+1
    if c>1:
        if ([n[i],c]) not in a:
            a.append([n[i],c])
    else:
        a.append(n[i])

    i=i+1
print(a)


n=["a","a","b","c","d","d","d","d","a","d","n","s","s"]
i=0
a=[]
while i<len(n):
    j=0
    c=0
    while j<len(n):
        if n[i]==n[j]:
            c=c+1
        j=j+1
    if c>1:
        if ([n[i],c]) not in a:
            a.append([n[i],c])
    else:
        a.append(n[i])
    i=i+1
print(a)

    

    


