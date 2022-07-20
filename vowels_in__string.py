s=input()
a='aeiouAEIOU'
c=0
b=[]
for i in s:
    if i in a:
        b.append(i)
        c+=1
if c==0:
    print(-1)
else:
    d=[]
    for i in b:
       if i not in d:
           d.append(i)
    print(*d)