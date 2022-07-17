s=input()
s=s.lower()
d=[]
for i in s:
    if i==' ':
        continue
    d.append(i)
d=set(d)
print(len(d))
