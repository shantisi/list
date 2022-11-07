# 33. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]


# n=[12,67,98,34]
# i=0
# b=[]
# while i<len(n): 
#     c=n[i]%10
#     d=n[i]//10
#     e=c+d
#     b.append(e)
#     i=i+1
# print(b)

# a=[[12,34],[23,34],[45,56]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         s=a[i][j]%10
#         c=a[i][j]//10
#         d=s+c
#         b.append(d)
#         j=j+1
#     i=i+1
# print(b)

a=["10","120"]
i=0
k=[]
b=[]
while i<len(a):
    d=str(a[i])
    s=""
    j=0
    while j<len(d):
        if d[j]!="0":
            s=s+d[j]
            k.append(int(s))
        else:
            pass
        j=j+1
    b.append(s)
    i=i+1
print(b)