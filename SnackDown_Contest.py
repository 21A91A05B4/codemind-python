t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=[]
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
    c.sort()
    c=set(c)
    for i in range(1,n+1):
        d.append(i)
    if(len(c)==len(d)):
        print('YES')
    else:
        print('NO')