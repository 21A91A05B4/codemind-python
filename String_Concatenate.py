s1=input()
s2=input()
d=[]
for i in s1:
    d.append(ord(i))
for i in s2:
    d.append(ord(i))
d.sort()
for k in d:
    print(chr(k),end='')