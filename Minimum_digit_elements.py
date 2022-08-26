n=int(input())
l=list(map(int,input().split()))
min=999
c=1
dc=0
f=[]
for i in l:
    dc=0
    while(i):
        r=i%10
        i=i//10
        dc+=1
    f.append(dc)
f.sort()
for i in f:
    if (i<min):
        min=i
    elif (i==min):
        c+=1
    else:
        continue
print(c)
