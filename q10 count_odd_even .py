elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
while i<len(elements):
    if elements[i]%2==0:
        count=count+1
        print(elements[i],[count],"even")
    else:
        count=count+1
        print(elements[i],[count],"odd")
    i=i+1
print("count",count)