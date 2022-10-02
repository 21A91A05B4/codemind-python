t=int(input())
while(t>0):
    m,n=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for i in a:
        l.append(i)
    for i in b:
        l.append(i)
    l.sort()
    print(*l)