t=int(input())
for i in range(t):
    c=0
    n=int(input())
    b=bin(n)
    s=str(b)
    for i in s:
        if(i=='1'):
            c+=1
    print(c)