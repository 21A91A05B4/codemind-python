t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    a=a[::-1]
    for i in range(len(a)):
        for j in range(i,len(a)):
            if(a[j]<a[i]):
                break
        else:
            c+=1
    print(c)