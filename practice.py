# a= [1,0,0]
# i=-1
# b=0
# sum=0
# while i>=-len(a):
#     sum=sum+(a[i])*2**b
#     b=b+1
#     i=i-1
# print(sum)

# n=int(input("enter the num"))
# i=0
# b=[]
# while i <(n):
#     c=int(input("enter the num"))
#     b.append(c)
#     i=i+1
# print(b)

# a=int(input("enter the number :"))
# i=0
# b=[]
# e=[]
# f=[]
# while i<=a:
#     c=int(input("enter the number :"))
#     b.append(c)
#     e.append(c)
#     s=b+e
#     f.append(s)
#     i=i+1
# print(f)


# a="priya"
# s=""
# i=1
# while i<=len(a):
#     print(a[-i]*2,end="")
#     i=i+1


# def addition():
#     a=10
#     b=5
#     c=a+b
# addition()
# def culculater(a,b):
#     if c=="+":
#         addition()
# culculater(10,5,"+")


# a="priya"
# d={}
# for i in a:
#     c=0
#     for j in a:
#         if i==j:
#             c=c+1
#             d[i]=c
# print(d)

# a="pooja"
# d=[]
# for i in a:
#     c=0
#     for j in a:
#         if i==j:
#             c=c+1
#         d.append(c)
# print(d)

# a=[[5,6,9],8,[6,5,3],7,[9,8,7]]
# i=0
# z=0
# b=[]
# while i<len(a):
#     if (type(a[i])is not list):
#         x=i-1
#         a[x].insert(j,(a[i]))
#     else:
#         j=0
#         while j<len(a[i]):
#             j=j+1
#     i=i+1
# print(a)

# o/p [[5,6,9,8],8,[6,5,3,7],7,[9,8,7]]


    #    (Disending Order)

# a=[3,5,7,2,1,23,4,6]
# for i in range(len (a)):
#     for j in range (len (a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# o/p [23,7,6,5,4,3,2,1]
      
    #   (Asending Order)

# a=[3,5,7,2,1,23,4,6]
# for i in range(len (a)):
#     for j in range (len (a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# o/p[1,2,3,4,5,6,7,23]




# a=int(input("enter the main dict"))
# q={}
# for i in range(a):
#     key=(input("enter the main key"))
#     size=int(input("enter the size of nested dict"))
#     s={}
#     for j in range(size):
#         n=int(input("enter the "))
#         value=input("enter the value")
#         s[n]=value
#     q[key]=s
# print(q)

# a=int(input("enter the main dict"))
# q={}
# for i in range(a):
#     key=(input("enter the main key"))
#     size=int(input("enter the size of nested dict"))
#     s={}
#     t=[]
#     for j in range(size):
#         n=int(input("enter the "))
#         value=input("enter the value")
#         t.append(value)
#         s[n]=t
#     q[key]=s
# print(q)

    #    (Nested List)
# a=int(input("enter the number :"))
# i=0
# b=[]
# e=[]
# f=[]
# while i<=a:
#     c=int(input("enter the number :"))
#     b.append(c)
#     e.append(c)
#     s=b+e
#     f.append(s)
#     i=i+1
# print(f)

# a="36700970098700"
# s=""
# s1=""
# for i in (a):
#     if i=="0":
#         s=s+i
#     else:
#         s1=s1+i
# print(s+s1)

# o/p  0000003677987

# a=["Poo@j#a22","niki23ta",]
# i=0
# d=[]
# while i <len(a):
#     str=" "
#     j=0
#     while j <len(a[i]):
#         if a[i][j]>=("a") and a[i][j]<="z" or a[i][j]>="A" and a[i][j]<="Z":
#             str=str+(a[i][j])
#         j=j+1
#     d.append(str)
#     i=i+1
# print(d)

# o/p ["pooja","nikita"]


# x=int(input("enter the num"))
# y=int(input("enter the num"))
# if x>=y:
#     print("max")
# else:
#     print("not max")


#    (interview question)

# a=["ram","mom","nitin","dad","mohan"]
# i=0
# b=[]
# c=0
# while i<len(a):
#     rev=(a[i][::-1])
#     if a[i]==rev:
#         b.append(a[i])
#         c=c+1
#     i=i+1
# print(c,b,"palindrom")



# a=["sonam","man","bad","nana","ram"]
# i=0
# b=[]
# while i<len(a):
#     rev=(a[i][::-1])
#     b.append(rev)
#     i=i+1
# print(b)


# a=["nitin","man","ram"]
# b=[["priya",20] ,["pooja",15],["ram",18]]
# i=0
# n={}
# open=[]
# while i<len(b):
#     n.update({a[i]:{"sarname":b[i][0],"age":b[i][1]}})
#     i=i+1
# open.append(n)
# print(open)

        # (voweles count)

# a=["priya","rani","dad","ram"]
# i=0
# d=[]
# while i <len(a):
#     j=0
#     c=0
#     while j<len(a[i]):
#         if a[i][j]=="a" or a[i][j]=="e" or a[i][j]=="i" or a[i][j]=="o" or a[i][j]=="u":
#             c=c+1
#         j=j+1
#     i=i+1
#     d.append(c)
# print(d)


# a=["shonam","rohan","pooja","nikita"]
# i=0
# b=[]
# while i<len(a):
#     s=a[i]
#     print(len(s))
#     i=i+1

# a=int(input("enter the num"))
# b=int(input("enter the num"))
# c=int(input("enter the num"))
# if a>b and a<c or a<b and a>c:
#     print(a)
# elif b>a and b<c or b<a and b>c:
#     print(b) 
# elif c>a and c<b or c<a and c>b:
#     print(c)
# else:
#     print("no")


    #    (reverse)
# 1. Reverse an array 
# a=[5,3,4,6,7,8,9]
# b=[]
# for i in a:
#     b=[i]+b
# print(b)

    #  (2) 
# d=[3,2,4,5,6,7]
# c=1
# n=[]
# for i in (d):
#     c=c+1
#     b=d[1-c]
#     n=n+[b]
# print(n)

        #  (mean)
# 2. Find the mean, median, and mode in an array 
# a=[1,2,3,4,5,6,7,8]
# s=0
# c=0
# for i in (a):
#     c=c+1
#     s=s+i
# print(s/c)

        #  (midian)
# a=[2,3,1,2,3,4,7,5,4,5,7,6,4,2,3]
# c=0
# for i in (a):
#     c=c+1
#     z=c//2
# print(a[z])

        #  ( mode )
# a=[1,1,2,3,3,4,5,5,]
# b=[]
# for s in a:
#     c=0
#     for j in a:
#         if s==j:
#             c=c+1
#     if c>1:
#         if s not in b:
#             b=b+[s]
# print(b)

        #  (dublicates)
# 4. Find duplicate elements in an array|
# a=[1,2,6,4,2,6]
# d=[]
# for i in (a):
#     c=0
#     for t in a:
#         if i==t:
#             c=c+1
#     if c>1:
#         if i not in d:
#             d=d+[i]
# print(d)

    

    #    (marjing 2 list, disending)
# 5. Merge two sorted arrays into a single sorted array
#  
# a1=[1,2,3,4,5]
# a2=[6,7,8,9,10]
# a=a1+a2
# c=0
# for i in a:
#     k=0
#     for j in a:
#         if a[c]>=a[k]:
#             a[c],a[k]=a[k],a[c]
#         k=k+1
#     c=c+1
# print(a)
 
        #  (assending)
# a1=[1,2,3,4,5]
# a2=[10,9,8,7,6,]
# a=a1+a2
# c=0
# for i in a:
#     k=0
#     for j in a:
#         if a[c]<=a[k]:
#             a[c],a[k]=a[k],a[c]
#         k=k+1
#     c=c+1
# print(a)

# 7. Find the Union and Intersection of the two sorted arrays          
# a=[1,2,6,4,2,6]
# b=[6,7,8,9,10,11]
# for i in (a):
#     b=b+[i]
# d=[]
# for i in b:
#     if i not in d:
#         d=d+[i]
# c=0
# for i in d:
#     k=0
#     for j in d:
#         if d[c]<=d[k]:
#             d[c],d[k]=d[k],d[c]
#         k=k+1
#     c=c+1
# print(d)


    #  (selection sort)
# a=[1,4,3,2,5,6]
# c=0
# for i in a:
#     f=0
#     for j in a:
#         if a[c]<=a[f]:
#             a[c],a[f]=a[f],a[c]
#         f=f+1
#     c=c+1
# print(a)

    #    (Bubble sort)
# a=[5,6,7,8,3,4,5]
# c=0
# for i in a:
#     n=0
#     for j in a:
#         if a[c]<=a[n]:
#             v=a[c]
#             a[c]=a[n]
#             a[n]=v
#         n=n+1
#     c=c+1
# print(a)


# 9. Find a number using Binary Search in a sorted array 

# n=[2,3,4,5,6,7,8]
# i=0
# b=[]
# while i<len(n):
#     s=" "
#     while n[i]>0:
#         c=(n[i]%2)
#         s=s+(str(c))
#         n[i]=n[i]//2
#     i=i+1
#     b=b+[s]
# l=[]
# for j in b:
#     s=j
#     t=1
#     r=""
#     for o in s:
#         r=r+(s[-t])
#         t=t+1
#     l=l+[r]
# print(l)


# 8. Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays. 

# a=[1,2,3,4,5,6,7]
# b=[8,9,10,11,12,13,14,3,5]
# c=0
# c1=0
# for i in a:
#     c=c+1
#     z=c//2
# for j in b:
#     c1=c1+1
#     y=c1//2 
# print(a[z])
# print(b[y])

# g=int(input("enter the number"))
# d=[3,6,7,5,10]
# e=[]
# a=0
# for i in d:
#     for j in d:
#         if i+j==g:
            
#             break
#             print(i,j)
            













