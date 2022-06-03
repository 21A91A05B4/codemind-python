n=int(input())
a=list(map(int,input().split()))
min=9999
for i in range(len(a)):
    if min>a[i]:
        min=a[i]
for i in range(min,0,-1):
    f=0
    for j in range(len(a)):
        if a[j]%i!=0:
            f=1
            break
    if f==0:
        print(i)
        break