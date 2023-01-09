t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    x=a[0]
    y=a[1]
    for i in range(1,y):
        if(x==0):
            print('0')
            break
        elif((i*i)%y==x):
            print(i)
            break
    else:
        print('-1')