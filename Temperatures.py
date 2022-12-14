n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        if(l[j]>l[i]):
            c.append(j-i)
            break
    else:
        c.append(0)
print(*c)        