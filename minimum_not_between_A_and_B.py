n=int(input())
a=list(map(int,input().split()))
l,r=map(int,input().split())
m=999
c=0
for i in a:
    if i>=l and i<=r:
        continue
    if m>i:
        m=i
        c+=1
if c==0:
    print(-1)
else:
    print(m)