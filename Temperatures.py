n=int(input())
a=list(map(int,input().split()))
c=[]
#print(a)
for i in range(len(a)):
    for j in range(i,len(a)):
        if(a[j]>a[i]):
            c.append(j-i)
            break
    else:
        c.append(0)
print(*c)        
    
    
    