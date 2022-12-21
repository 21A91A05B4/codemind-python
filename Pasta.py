n1,n2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
if(n1<n2):
    print('No')
else:
    for i in b:
        if i in a and b.count(i)<=a.count(i):
            c+=1
    if(c==0):
        print('No')
    else:
        print('Yes')
    