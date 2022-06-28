def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
def fun(s):
    for i in range(1,20):
        t=s+i
        if(prime(t)):
            return i

a=int(input())
b=int(input())
s=a+b
k=fun(s)
print(k)