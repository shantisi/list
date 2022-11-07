


name=["m","o","m"]
rev=(name[::-1])
if rev==name:
    print("palindrom")
else:
    print("not palindrom")

name=["m","o","m"]
i=0
rev=1
while i<=len(name) and rev<=len(name):
    b=name[i]
    c=name[-rev]
    i=i+1
    rev=rev+1
if b==c:
    print("palendrome")
else:
   print("not palendrome")




a=["n","i","t","i","n"]
i=1
b=[]
while i<=len(a):
    b.append(a[-i])
    i=i+1
if b==a:
    print("palindrom")
else:
    print("not palindrom")
