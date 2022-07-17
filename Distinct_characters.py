s=input()
s=s.lower()
d=[]
f=0
for i in s:
    if i==' ':
        continue
    if(s.count(i)==1):
        d.append(ord(i))
        
d.sort()
for i in d:
    print(chr(i),end='')