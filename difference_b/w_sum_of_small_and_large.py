s=input()
e=0
f=0
d=[]
for i in s.split():
    d.append(i)
for i in d:
    e=e+ord(max(i))
    f=f+ord(min(i))
print(e-f)