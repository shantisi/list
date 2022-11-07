a=int(input("enter no"))
if a>100 and a<999:
    num=a%10
    sum=a//10
    a=sum%10
    b=a%10
    a=(str(num)+str(sum)+str(a)+str(b))
    print(a)
else:
    print("not 3 digit no")

# 29. Remove empty List from List
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

list=[5,6,[],3,[],[],9]
i=0
a=[]
while i<len(list):
    if list[i]!=[]:
        a.append(list[i])
    i=i+1
print(a)

num =int(input("enter no"))
i=0
sum=0
a=[]
while i<num:
    n=int(input("enter no"))
    a.append(n)
    if a[i]%2==0:
        sum =sum+a[i]
    i=i+1
print(a)
print(sum)


list=[5,6,[],3,[],[],9]
i=0
a=[]
while i<len(list):
    if list[i]!=[]:
        a.append(list[i])
    i=i+1
print(a)