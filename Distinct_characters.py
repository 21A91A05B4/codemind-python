s=input()
s=s.lower()
b=[]
for i in s:
    if i==' ':
        continue
    if s.count(i)==1:
        b.append(ord(i))
b.sort()
for i in b:
    print(chr(i),end='')