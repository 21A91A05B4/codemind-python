n=int(input())
a=list(map(int,input().split()))
l,r=map(int,input().split())
max=0
c=0
for i in a:
    if i>=l and i<=r:
        if i>max:
            max=i
            c+=1
if c==0:
    print(-1)
else:
    print(max)