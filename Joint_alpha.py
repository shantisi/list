list=["g","f","g",["i","s"],["b","e","s","t"]]
i=0
sum=""
while i<len(list):
    j=0
    while j<len(list[i]):
        sum=sum+list[i][j]
        j=j+1
    i=i+1
print(sum)
      