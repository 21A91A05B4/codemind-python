n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
i=0
j=0
b=[]
while i<len(e) and j<len(o):
    b.append(e[i])
    b.append(o[j])
    i+=1
    j+=1
while i<len(e):
    b.append(e[i])
    i+=1
while j<len(o):
    b.append(o[j])
    j+=1
if len(b)%2!=0:
    b.append(0)
print(*b)