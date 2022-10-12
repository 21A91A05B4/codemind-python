a,b=map(int,input().split())
z=list(map(int,input().split()))
m=0
#print(b) 
#print (*z) 
s=0
for i in z:
    if i<=b:
        #print(i) 
        m+=1
    else:
        s+=1
    if s>1:
        break
print(m)