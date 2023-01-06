t=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if(a.count(i)!=2):
        c.append(i)
c.sort()
print(*c)