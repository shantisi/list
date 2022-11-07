list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i<len(list):
    j=0
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        j=j+1
    if [list[i],c] not in a:
        a.append([list[i],c])
    i=i+1
print(a)

