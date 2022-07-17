s=input()
s=s.lower()
f=0
for i in s:
    if i==' ':
        continue
    if(s.count(i)==1):
        f+=1
print(f)