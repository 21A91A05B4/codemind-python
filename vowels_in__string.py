s=input()
a='aeiouAEIOU'
b=[]
c=0
for i in s:
    if i in a:
        c+=1
        b.append(i)
if(c==0):
    print('-1')
else:
    l=[]
    for i in b:
        if i not in l:
            l.append(i)
    print(*l)