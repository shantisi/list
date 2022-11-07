# Write a Python program to find the dimension of a given matrix.
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
# [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
# [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)


n=[[0, 1, 2], [2, 4, 5]]
i=0
c=0
c1=0
while i<len(n):
    c=c+1
    c1=0
    j=0
    while j<len(n[i]):
        c1=c1+1
        j+=1
    i+=1
print((c,c1))


n=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
i=0
c=0
c1=0
while i<len(n):
    c=c+1
    c1=0
    j=0
    while j<len(n[i]):
        c1=c+1
        j=j+1
    i=i+1
print(c,c1)


i=1
sum=0
while i<=10:
    if i<=5:
        sum=sum+i
        print(sum)
    elif i>=5:
        print(i*i)
    i=i+1
