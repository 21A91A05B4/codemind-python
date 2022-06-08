l=int(input())
r=int(input())
for i in range(l,r+1):
    r=0
    t=i
    while i:
        d=i%10
        i=i//10
        r=(r*10)+d
    if(t==r):
        print(t,end=' ')