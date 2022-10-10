n=int(input())
a=list(map(int,input().split()))
e=0
k=len(a)-1
b=[]
while e<k:
    b.append(a[e])
    b.append(a[k])
    e+=1
    k-=1
if len(a)%2!=0:
    b.append(a[n//2])
    b.append(0)
    print(*b)
else:
    print(*b)
    