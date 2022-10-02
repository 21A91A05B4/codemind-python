T=int(input())
while(T>0):
    s=input()
    if s==(s[::-1]):
        print('YES',end=' ')
        if len(s)%2==0:
            print('EVEN')
        else:
            print('ODD')
    else:
        print('NO')
    T-=1