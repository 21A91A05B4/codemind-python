s=input()
s=s.split()
q=[]
e=''
for i in s[::-1]:
    q.append(i)
    e+=i
    break
b=[]
for i in e:
    b.append(ord(i))
v=min(b)
d=v+32
if d in b:
    print(chr(d))
else:
    print(chr(v))