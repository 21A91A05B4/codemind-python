def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
#m=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if(prime(i)):
            continue
        else:
            c+=1
print(c)
    