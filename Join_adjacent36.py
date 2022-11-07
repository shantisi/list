# 36. Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']

n=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
a=[]
while i<len(n):
    b=(n[i+1])+(n[i])
    a.append(b)
    i=i+2
print(a)                                                                                           


n=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
b=[]
while i<len(n):
    a=n[i]+n[i+1]
    b.append(a)
    i=i+2
print(b)



