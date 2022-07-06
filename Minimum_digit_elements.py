n=int(input())
a=list(map(int,input().split()))
min=9999
for i in a:
    if(i<min):
        min=i
b=min
f=0
c=0
while(b):
    r=b%10
    b=b//10
    c+=1
for i in range(len(a)):
    dc=0
    while(a[i]):
        d=a[i]%10
        a[i]=a[i]//10
        dc+=1
    if(dc==c):
        f+=1
    i+=1
print(f)
        
    