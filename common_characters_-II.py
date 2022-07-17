s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
d=[]
e=[]
f=[]
c=0
for i in s1:
        if i==' ':
            continue
        else:
           d.append(i)
for i in s2:
    if i==' ':
            continue
    else:
        e.append(i)
d=set(d)
e=set(e)
for i in d:
    if i in e:
        c+=1

print(c)
    
