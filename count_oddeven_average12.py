elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0 
counteven=0
countodd=0
countallnum=0
sumeven=0
sumodd=0
sumallnum=0
avgeven=0
avg1odd=0
avg2allnum=0
while i<len(elements):
    if elements[i]%2==0:
        sumeven=sumeven+elements[i]
        counteven=counteven+1
        avgeven=sumeven/4
    if elements[i]%2!=0:
        sumodd=sumodd+elements[i]
        countodd=countodd+1
        avg1odd=sumodd/7
    if elements[i]%1==0:
        sumallnum=sumallnum+elements[i]
        countallnum=countallnum+1
        avg2allnum=sumallnum/11
    i=i+1
print("counteven",counteven)
print("countodd",countodd)
print("countallnum",countallnum)
print("sumeven",sumeven)
print("sumodd",sumodd)
print("sumallnum",sumallnum)
print("avgeven",avgeven)
print("avgodd",avg1odd)
print("avg2all",avg2allnum)