n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
if(n<m):
    print('No')
else:
    for i in b:
        if i in a and b.count(i)<=a.count(i):
            c+=1
    if(c==0):
        print('No')
    else:
        print('Yes')