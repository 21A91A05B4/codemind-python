n=int(input())
a=list(map(int,input().split()))
if(a[0]<a[1]):
    b=[]
    d=[]
    c=0
    for i in range(len(a)):
        if(i%2==0):
            b.append(a[i])
        else:
            d.append(a[i])
    for i in range(len(a)//2):
        if(b[i]>d[i]):
            c=1
            break
    if(c==1):
        print('no')
    else:
        print('yes')
else:
    b=[]
    d=[]
    c=0
    for i in range(len(a)):
        if(i%2==0):
            b.append(a[i])
        else:
            d.append(a[i])
    for i in range(len(a)//2):
        if(b[i]<d[i]):
            c=1
            break
    if(c==1):
        print('no')
    else:
        print('yes')