n1,n2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=[]
for i in a:
    if i not in b:
        e.append(i)
for i in b:
    if ((i not in a) and(i not in e)):
        e.append(i)
f=[]
for i in e:
    if i not in f:
        f.append(i)
print(*f)