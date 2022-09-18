s=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
c=0
min=999
for i in a:
    if i>=m and i<=n:
         if min>i:
             min=i
             c+=1
if c==0:
    print(-1)
else:
    print(min)