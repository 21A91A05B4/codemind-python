def ispalin(n):
    r=0
    t=n
    while(t):
        d=t%10
        t=t//10
        r=r*10+d
    if n==r:
        return True
    return False
def reverse(n):
    s=0
    while(n):
        m=n%10
        n=n//10
        s=s*10+m
    return s
x=int(input())
x=x+reverse(x)
while(1):
    if ispalin(x):
         print(x)
         break
    else:
         x=reverse(x)+x