def faktoriyel(x):
    a=1
    for i in range(1,x+1):
        a*=i
    return a    
sum1=[]
for i in range(3,2540160):
    a=0
    for b in str(i):
        a+=faktoriyel(int(b))
    if a==i:
        sum1.append(a)
    a=0
print(sum(sum1))    

