def prime(i):
    if i==1:
        return 0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
    return 1
s=int(input())
a=list(map(int,input().split()))
m=min(a)
m1=a.index(m)
n=max(a)
n1=a.index(n)
c=0
for i in range(min(m1,n1),max(m1,n1)+1):
    if prime(a[i]):
        c+=1
print(c)