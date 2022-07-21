n=int(input())
a=list(map(str,input().split()))
s=''
for i in a:
    s=s+i
t=int(s)
t=t+1
d=str(t)
b=[]
for i in d:
    b.append(i)
print(*b)