def fac(n):
    fac=1
    while(n>0):
        fac=fac*n
        n-=1
    return fac
n=int(input())
t=n
s=0
while n>0:
    d=n%10
    n=n//10
    s=s+fac(d)
if s==t:
    print('The number {0} is a strong number'.format(t))
else:
    print('The number {0} is not a strong number'.format(t))