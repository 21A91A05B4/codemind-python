n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in a:
    s+=i
c=s%n
for i in range(n,0,-1):
    if(s%i==0):
        print(i)
        break
    
         
