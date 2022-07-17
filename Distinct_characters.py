s=input()
s=s.lower()
d=[]
e=[]
v=[]
f=0
for i in s:
    if i==' ':
        continue
    d.append(ord(i))
e=set(d)
for i in e:
    v.append(i)
v.sort()
for i in v:
    print(chr(i),end='')