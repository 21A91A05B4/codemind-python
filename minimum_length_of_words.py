s=input()
d=[]
a=[]
for i in s.split():
    d.append(i)
for i in d:
    a.append(len(i))
print(min(a))