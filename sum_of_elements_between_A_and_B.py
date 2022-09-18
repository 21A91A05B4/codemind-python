s=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
c=0
s=0
for i in a:
    if i>=m and i<=n:
         s=s+i
         c+=1
if c==0:
    print(-1)
else:
    print(s)