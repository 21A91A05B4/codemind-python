n=int(input())
a=list(map(int,input().split()))
#b=list(map(int,input().split()))
b=[]
#c=0
for i in a:
   # if i not in b and a.count(i)>1:
        b.append(i*i)
        #c+=1
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            t=b[i]
            b[i]=b[j]
            b[j]=t
print(*b)