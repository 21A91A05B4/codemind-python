s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
d=[]
c=0
for i in s1:
    if i in s2:
        if i==' ':
            continue
        if ord(i) not in d:
            d.append(ord(i))
            c+=1
if c==0:
    print(-1)
else:
    d.sort()
    for i in d:
        print(chr(i),end='')